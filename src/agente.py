import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ServerError

from config import GEMINI_API_KEY
from persona import obter_system_instruction
from database import buscar_contexto_huggingface

# Langfuse 4.x
from langfuse import observe, get_client, propagate_attributes


load_dotenv()

# Cliente singleton do Langfuse 4.x
langfuse = get_client()


class AgenteBio:
    def __init__(self, model_name: str = "gemini-3.5-flash-lite"):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model_name = model_name

    @observe(name="processar_mensagem_bio")
    def processar_mensagem(
        self,
        prompt_usuario: str,
        historico_chat: list
    ) -> tuple[str, str]:

        # No Langfuse 4.x, atributos de correlação como user_id e
        # tags são propagados para as observações filhas.
        with propagate_attributes(
            user_id="usuario_demo",
            tags=["financeiro", "faiss_rag"],
        ):
            # 1. Busca contexto no FAISS
            contexto_hf = self._buscar_contexto_faiss(prompt_usuario)

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

                messages.append(
                    {
                        "role": role,
                        "parts": [
                            {
                                "text": msg["content"]
                            }
                        ],
                    }
                )

            # Adiciona a mensagem atual
            messages.append(
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": prompt_usuario
                        }
                    ],
                }
            )

            # 2. Chamada à LLM
            try:
                resposta_texto = self._gerar_resposta_llm(
                    messages,
                    config
                )

                return resposta_texto, contexto_hf

            except ServerError as e:
                print(f"Erro de servidor detectado: {e}")

                # No Langfuse 4.x, atualizamos a observação ativa.
                langfuse.update_current_span(
                    metadata={
                        "error": str(e)
                    },
                    level="ERROR",
                    status_message=str(e),
                )

                return (
                    "⚠️ O servidor do Gemini está enfrentando uma "
                    "alta demanda ou instabilidade no momento. "
                    "Por favor, aguarde alguns segundos e tente "
                    "enviar sua mensagem novamente.",
                    "",
                )

            except Exception as e:
                print(f"Erro inesperado: {e}")

                langfuse.update_current_span(
                    metadata={
                        "error": str(e)
                    },
                    level="ERROR",
                    status_message=str(e),
                )

                return (
                    f"⚠️ Ocorreu um erro inesperado na comunicação "
                    f"com o agente: {str(e)}",
                    "",
                )

    @observe(name="faiss_search")
    def _buscar_contexto_faiss(self, prompt: str) -> str:
        """Mede o tempo gasto exclusivamente na busca vetorial."""
        return buscar_contexto_huggingface(prompt)

    @observe(name="gemini_generation")
    def _gerar_resposta_llm(
        self,
        messages: list,
        config: types.GenerateContentConfig
    ) -> str:
        """Mede o tempo gasto exclusivamente na resposta do Gemini."""

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=messages,
            config=config
        )

        return response.text