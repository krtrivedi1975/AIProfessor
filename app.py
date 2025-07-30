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
