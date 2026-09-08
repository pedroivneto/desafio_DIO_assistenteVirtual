from google import genai
from google.genai import types
from google.genai.errors import ServerError
from config import GEMINI_API_KEY
from persona import obter_system_instruction
from database import buscar_contexto_huggingface

class AgenteBio:
    def __init__(self, model_name: str = "gemini-3.5-flash-lite"):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model_name = model_name

    def processar_mensagem(self, prompt_usuario: str, historico_chat: list) -> str:
        # Step B -> Consulta a base do Hugging Face com base na dúvida inserida
        contexto_hf = buscar_contexto_huggingface(prompt_usuario)

        # Monta a System Instruction unificada
        system_instruction_base = obter_system_instruction()
        system_instruction_completo = f"""
{system_instruction_base}

### CONTEXTO DA BASE DE DADOS HUGGING FACE (Sujet & Snorkel AI):
Use os dados abaixo como referência fundamentada para construir sua resposta:
{contexto_hf}
"""

        config = types.GenerateContentConfig(
            system_instruction=system_instruction_completo,
            temperature=0.1,
        )
  
        # Formata o histórico da conversa
        messages = []
        for msg in historico_chat:
            role = "user" if msg["role"] == "user" else "model"
            messages.append({"role": role, "parts": [{"text": msg["content"]}]})

        messages.append({"role": "user", "parts": [{"text": prompt_usuario}]})

            # 💡 1. GRAVAÇÃO DO LOG DE PROMPTS (Antes de enviar para a LLM)
        try:
            with open("historico_prompts.log", "a", encoding="utf-8") as f_prompts:
                f_prompts.write(f"\n{'-'*80}\n")
                f_prompts.write(f"📝 PERGUNTA ORIGINAL DO USUÁRIO:\n{prompt_usuario}\n\n")
                f_prompts.write(f"⚙️ SYSTEM INSTRUCTION ENVIADO:\n{system_instruction_completo}\n")
                f_prompts.write(f"{'-'*80}\n")
        except Exception as e_log:
            print(f"Aviso: Falha ao salvar log de prompts: {e_log}")

    # Proteção adicionada para evitar que o app quebre se o Gemini estiver fora do ar    
        try:
            # Step B -> C (Envia para o Gemini)
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=messages,
                config=config
            )
           # 💡 2. GRAVAÇÃO DO LOG DE RESPOSTAS (Para análise futura com Machine Learning)
            try:
                with open("log_qualidade_respostas.txt", "a", encoding="utf-8") as f_respostas:
                    f_respostas.write(f"--- NOVA RESPOSTA GERADA ---\n")
                    f_respostas.write(f"CONTEXTO DO FAISS:\n{contexto_hf}\n\n")
                    f_respostas.write(f"RESPOSTA DO BIO:\n{response.text}\n")
                    f_respostas.write(f"{'='*50}\n")
            except Exception as e_resp:
                print(f"Aviso: Falha ao salvar log de respostas: {e_resp}")

            # Retorna com sucesso as 2 variáveis esperadas pelo app.py
            return response.text, contexto_hf
    
        except ServerError as e:
            print(f"Erro de servidor detectado: {e}")
            # 💡 CORREÇÃO: Retorna o aviso E uma string vazia para manter os 2 valores estáveis!
            return "⚠️ O servidor do Gemini está enfrentando uma alta demanda ou instabilidade no momento. Por favor, aguarde alguns segundos e tente enviar sua mensagem novamente.", ""
            
        except Exception as e:
            print(f"Erro inesperado: {e}")
            # 💡 CORREÇÃO: Retorna o erro E uma string vazia para o app.py não quebrar!
            return f"⚠️ Ocorreu um erro inesperado na comunicação com o agente: {str(e)}", ""

    