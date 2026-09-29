# FinWise AI

Assistente de Educação Financeira baseado em IA, desenvolvido com arquitetura RAG (Retrieval-Augmented Generation), Google Gemini, FAISS e Sentence Transformers.

O FinWise AI combina busca semântica, recuperação vetorial e modelos de linguagem para fornecer respostas contextualizadas sobre finanças pessoais.

🇺🇸 English version available: [README.md](README.md)

---

## Funcionalidades

✅ Arquitetura RAG

✅ Busca Semântica com FAISS

✅ Base de Conhecimento Financeira

✅ Integração com Google Gemini

✅ Embeddings com Sentence Transformers

✅ Observabilidade com Langfuse

✅ Histórico de Conversação

✅ Interface Streamlit

✅ Gerenciamento Seguro de Credenciais

---

## Visão Geral

O assistente foi desenvolvido para fornecer orientação financeira educacional de forma contextualizada.

Antes de gerar uma resposta, a aplicação realiza uma busca semântica em uma base de conhecimento financeira. Os documentos mais relevantes são recuperados e incorporados ao contexto enviado ao modelo Gemini.

Essa abordagem aumenta a relevância e a consistência das respostas geradas.

---

## Arquitetura

```text
Usuário
  │
  ▼
Streamlit
  │
  ▼
Agente
  │
  ├── Persona
  │
  └── Busca Vetorial
          │
          ▼
         FAISS
          │
          ▼
Contexto Recuperado
          │
          ▼
 Google Gemini
          │
          ▼
Resposta Final
```

---

## Stack Tecnológica

### Backend

- Python 3.12

### IA Generativa

- Google Gemini
- Google GenAI SDK
- Sentence Transformers
- Hugging Face Datasets

### Busca Vetorial

- FAISS CPU
- NumPy

### Observabilidade

- Langfuse

### Interface

- Streamlit

### Utilitários

- Pandas
- Scikit-Learn
- SciPy
- PyArrow
- python-dotenv

---

## Pipeline RAG

O fluxo principal é:

1. Usuário envia uma pergunta.
2. A pergunta é convertida em embedding.
3. O FAISS realiza busca semântica.
4. Documentos relevantes são recuperados.
5. Contexto recuperado é combinado com as instruções do sistema.
6. O Gemini gera a resposta final.

Modelo de embeddings:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

## Base de Conhecimento

O projeto utiliza como fonte de dados conjuntos públicos do Hugging Face:

- sujet-ai/Sujet-Finance-Instruct-177k
- snorkelai/agent-finance-reasoning

Os documentos são transformados em embeddings e armazenados em uma base vetorial para consulta semântica.

---

## Observabilidade

O Langfuse é utilizado para monitorar:

- Avaliação automática da qualidade das respostas
- Detecção de alucinações
- Pontuação de aderência ao contexto recuperado (Groundedness Score)
- Pipeline de avaliação utilizando LLM como juiz (LLM-as-a-Judge)

---

## Estrutura do Projeto

```text
finwise-ai/
│
├── logs/
│
├── src/
│   ├── agente.py
│   ├── app.py
│   ├── database.py
│   ├── config.py
│   └── persona.py
│
├── .gitignore
├── .env.example
└── README.md
```

---

## Execução Local

Criar ambiente virtual:

```bash
python -m venv .venv
```

Ativar:

```bash
source .venv/bin/activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

Criar arquivo .env:

```env
GEMINI_API_KEY=
LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

Executar:

```bash
streamlit run src/app.py
```

---

## Segurança

Credenciais são carregadas através de variáveis de ambiente e nunca devem ser incluídas diretamente no código.

Arquivos sensíveis como `.env` não devem ser versionados.

---

## Limitações

O assistente possui finalidade exclusivamente educacional.

As respostas geradas por LLMs podem conter erros e não substituem orientação profissional especializada.

---

## Melhorias Futuras

- Avaliação automática da qualidade das respostas
- Detecção de alucinações
- Métricas de groundedness (aderência ao contexto recuperado)
- Pipeline de avaliação baseado em LLM-as-a-Judge

---

## Autor

Pedro Ivan Neto

Projeto desenvolvido para estudo de IA Generativa, RAG, observabilidade, engenharia de prompts e desenvolvimento assistido por IA.

---

## Licença

MIT License