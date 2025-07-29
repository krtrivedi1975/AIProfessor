import openai
import streamlit as st

st.title("Ask Your AI Professor")

openai.api_key = st.secrets["openai_api_key"]

question = st.text_input("Ask a question:")

if question:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful, clear, and friendly university professor."},
                {"role": "user", "content": question}
            ]
        )
        answer = response['choices'][0]['message']['content']
        st.write("🧑‍🏫 AI Professor says:")
        st.success(answer)
