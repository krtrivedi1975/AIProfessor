import openai
import streamlit as st

st.title("Ask Your AI Professor")

openai.api_key = st.secrets["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"]

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
