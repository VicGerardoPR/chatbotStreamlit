import streamlit as st
from transformers import pipeline

# Configura el pipeline del chatbot utilizando un modelo de Hugging Face
chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

# Configura la aplicación de Streamlit
st.title("Chatbot con Hugging Face y Streamlit")
st.write("¡Hola! Soy un chatbot impulsado por Hugging Face. ¿En qué puedo ayudarte hoy?")

# Inicializa el historial de conversación
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Función para obtener respuesta del chatbot
def get_chatbot_response(user_input):
    response = chatbot(user_input)
    return response

# Entrada del usuario
user_input = st.text_input("Tú: ", "")

if user_input:
    response = get_chatbot_response(user_input)
    st.session_state.conversation_history.append(f"Tú: {user_input}")
    st.session_state.conversation_history.append(f"Chatbot: {response[0]['generated_text']}")

# Mostrar el historial de conversación
for message in st.session_state.conversation_history:
    st.write(message)
