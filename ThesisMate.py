import streamlit as st
import google.generativeai as genai

api_key = st.secrets["api_key"]

genai.configure(api_key=api_key)

#Page setup
st.set_page_config(page_title="ChatMate", page_icon="🤖", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #00b4d8;'>🤖 Your ChatMate</h1>
    <p style='text-align: center; color: gray;'>ask anything — technical, academic, or creative questions</p>
    <hr>
""", unsafe_allow_html=True)

#Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Sidebar for info
with st.sidebar:
    st.title("💡 About")
    st.write("""
    This chatbot uses **Google Gemini 2.5 Flash** model.
    """)
    st.markdown("**Developed by:** Aqib Ahmed 💻")

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})

    # Generate AI response
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(user_input)
    st.session_state.messages.append({"role": "assistant", "text": response.text})

#Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(f"**You:** {msg['text']}")
    else:
        st.chat_message("assistant").markdown(f"**ChatMate:** {msg['text']}")
