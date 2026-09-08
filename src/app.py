import streamlit as st
from agente import AgenteBio

st.set_page_config(
    page_title="BIO - Agente Financeiro",
    page_icon="💰",
    layout="centered"
)

# Título grande e amigável
st.title("💚 Olá! Eu sou o BIO")
st.subheader("Seu expert em finanças contemporâneas e descomplicadas.")
st.info(
    "💡 **Como eu funciono?** Você pode me fazer perguntas simples como 'Como aumentar meu limite?' "
    "ou complexas como 'Como começar a investir na bolsa?'. Estou aqui para traduzir o economês para você!"
)

if "agente" not in st.session_state:
    st.session_state.agente = AgenteBio()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Olá! Sou o BIO, expert em finanças. Como posso te ajudar hoje?"
        }
    ]

# Exibe o histórico existente
for message in st.session_state.messages:
    avatar_atual = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar_atual):
        st.markdown(message["content"])

# Entradas do Cliente (A -> B)
if prompt := st.chat_input("Digite sua dúvida financeira..."):
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("BIO está consultando a base de dados..."):
            resposta_agente, fontes_usadas = st.session_state.agente.processar_mensagem(
                prompt_usuario=prompt,
                historico_chat=st.session_state.messages[:-1]
            )
            st.markdown(resposta_agente)

    # D -> A (Salva a resposta do agente)
    st.session_state.messages.append({"role": "assistant", "content": resposta_agente})