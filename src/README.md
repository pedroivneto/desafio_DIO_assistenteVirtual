# 💚 BIO - Agente Financeiro Inteligente (RAG)

O **BIO** é um assistente virtual contemporâneo desenvolvido como projeto prático para o laboratório da **DIO** (Digital Innovation One). O objetivo principal é ajudar usuários leigos a compreenderem finanças, traduzindo jargões econômicos complexos por meio de analogias simples do dia a dia.

A aplicação utiliza uma arquitetura **RAG** (Geração Aumentada por Recuperação) para buscar informações fundamentadas em bases de dados locais antes de gerar respostas com Inteligência Artificial, evitando alucinações.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**: Linguagem base do projeto.
- **Streamlit**: Interface gráfica amigável e interativa para o usuário.
- **Google GenAI SDK**: Integração com o modelo **Gemini 3.5-flash-lite** para geração de respostas com guardrails.
- **Sentence-Transformers**: Geração de *embeddings* (vetorização de texto) local via CPU.
- **FAISS (Facebook AI Similarity Search)**: Banco de dados vetorial para busca por similaridade de alta velocidade.
- **Hugging Face Datasets**: Utilização dos datasets `Sujet-Finance-Instruct-177k` e `agent-finance-reasoning` (modo streaming).

---

## 🧠 Arquitetura do Sistema: Como Funciona?

1. **Vetorização (Embeddings)**: Os dados textuais do Hugging Face são transformados em vetores numéricos representativos utilizando o `sentence-transformers`.
2. **Indexação (FAISS)**: O FAISS organiza esses vetores em um mapa matemático estruturado.
3. **Busca por Similaridade**: Quando o usuário envia uma mensagem, a pergunta é vetorizada e o FAISS localiza instantaneamente o contexto financeiro mais relevante.
4. **Prompt Engineering (Persona)**: O contexto recuperado é injetado junto à persona estruturada do **BIO** (expert, acolhedor e pedagógico) e enviado com segurança via API.
5. **Geração da Resposta**: O Gemini gera o texto final e o Streamlit exibe a resposta acompanhada das fontes consultadas.

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter o **Python 3.12** instalado.
2. Clone o repositório e acesse a pasta raiz.
3. Ative o ambiente virtual:
   ```bash
   source .venv/bin/activate
   ```
4. Instale as dependências utilizando o cache temporário local para otimização de disco:
   ```bash
   TMPDIR=~/tmp pip install -r src/requirements.txt
   ```
5. Crie um arquivo `src/config.py` e insira sua chave do Google AI Studio:
   ```python
   GEMINI_API_KEY = "SUA_CHAVE_AQUI"
   ```
6. Execute a aplicação a partir do diretório raiz:
   ```bash
   python -m streamlit run src/app.py
   ```

---

## 🛡️ Guardrails e Segurança

O agente possui travas de segurança rigorosas configuradas em sua persona:
- **Foco estrito**: Responde apenas a dúvidas de economia, investimentos e finanças.
- **Direcionamento dinâmico**: Caso o usuário pergunte sobre outros escopos (ex: mecânica automotiva), o agente recusa a resposta e direciona o usuário para o profissional correto de forma empática.
