import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Configura el tokenizador y el modelo LLaMA desde Hugging Face
tokenizer = AutoTokenizer.from_pretrained("meta-llama/LLaMA-7B")
model = AutoModelForCausalLM.from_pretrained("meta-llama/LLaMA-7B")

# Crear un pipeline de generación de texto
llama_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Configura la aplicación de Streamlit
st.title("Chatbot Streamlit")
st.write("¡Hola! ¿En qué puedo ayudarte hoy?")

# Inicializa el historial de conversación
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# Función para obtener respuesta del chatbot
def get_chatbot_response(user_input):
    response = llama_pipeline(user_input, max_length=100, num_return_sequences=1)
    message = response[0]['generated_text']
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
