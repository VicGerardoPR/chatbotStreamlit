import streamlit as st
import openai
import os

# Configura tu clave API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Configura la aplicación de Streamlit
st.title("Chatbot")
st.write("¡Hola! ¿En qué puedo ayudarte hoy?")

# Inicializa el historial de conversación
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Función para obtener respuesta del chatbot
def get_chatbot_response(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text.strip()
    return message

# Entrada del usuario
user_input = st.text_input("Tú: ", "")

if user_input:
    response = get_chatbot_response(user_input)
    st.session_state.conversation_history.append(f"Tú: {user_input}")
    st.session_state.conversation_history.append(f"Chatbot: {response}")

# Mostrar el historial de conversación
for message in st.session_state.conversation_history:
    st.write(message)
