import streamlit as st
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

@st.cache_resource
def inicializar_base_de_dados():
    """
    Carrega amostras dos datasets do Hugging Face e constrói o índice vetorial FAISS.
    """
    documents = []
    
    # 1. Carrega Sujet-Finance-Instruct-177k
    try:
        ds_instruct = load_dataset("sujet-ai/Sujet-Finance-Instruct-177k", split="train", streaming=True).take(1000)
        for item in ds_instruct:
            prompt = item.get("user_prompt", "") or item.get("instruction", "")
            resp = item.get("model_response", "") or item.get("output", "")
            if prompt and resp:
                documents.append(f"Instrução: {prompt}\nResposta Base: {resp}")
    except Exception as e:
        print(f"Erro ao carregar Sujet-Finance: {e}")

    # 2. Carrega agent-finance-reasoning
    try:
        ds_agent = load_dataset("snorkelai/agent-finance-reasoning", split="train", streaming=True).take(1000)
        for item in ds_agent:
            query = item.get("user_query", "") or item.get("query", "")
            reasoning = item.get("agent_trace", "") or item.get("response", "")
            if query and reasoning:
                documents.append(f"Consulta Agente: {query}\nRaciocínio: {reasoning}")
    except Exception as e:
        print(f"Erro ao carregar Agent-Finance-Reasoning: {e}")

    if not documents:
        documents.append("Base de conhecimento padrão sobre finanças pessoais e investimentos de baixo risco.")

    # Gera embeddings e cria o índice FAISS
    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = embedder.encode(documents, show_progress_bar=True)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype("float32"))
    
    return embedder, index, documents

def buscar_contexto_huggingface(query: str, top_k: int = 2) -> str:
    """
    Busca no índice vetorial o contexto mais relevante para o prompt inserido.
    """
    embedder, index, documents = inicializar_base_de_dados()
    query_vector = embedder.encode([query])
    distances, indices = index.search(np.array(query_vector).astype("float32"), top_k)
    
    contextos = []
    for idx in indices[0]:
        if idx < len(documents):
            contextos.append(documents[idx])
            
    return "\n---\n".join(contextos)