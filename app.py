import streamlit as st
from transformers import pipeline

st.title("AI Girlfriend ❤️")

st.write("Baat kariye apni AI Girlfriend se!")

# Loading pipeline
chatbot = pipeline("text-generation", model='PygMalionAI/pygmarion-6b', max_new_tokens=100)


# User input
prompt = st.text_input("Aap kya kahoge?")

if st.button("Send") and prompt:
    response = chatbot(prompt)
    st.write("AI Girlfriend:")
    st.write(response[0]["generated_text"])

# Note: Streamlit policy prefers SFW content
# Please avoid NSFW messages
