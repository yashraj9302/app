import streamlit as st
from queryRunner import run_query
from streamlit_speech_to_text import speech_to_text   

st.set_page_config(page_title="MallBuddy Chat", layout="wide")
st.title("Lido Mall Shopping Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 🎙️ --- Voice Input Section (ADD THIS BLOCK) ---
st.subheader("🎤 Speak to MallBuddy")
voice_text = speech_to_text(language='en')

if voice_text:
    st.session_state.messages.append({"role": "user", "content": voice_text})
    st.chat_message("user").markdown(voice_text)

    with st.chat_message("assistant"):
        with st.spinner("MallBuddy 🤖 is thinking..."):
            response = run_query(voice_text)

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# 🧑 --- Text Input Section (EXISTING CODE) ---
if prompt := st.chat_input("Ask me about shops, offers, food, movies..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("MallBuddy 🤖 is thinking..."):
            response = run_query(prompt)

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
