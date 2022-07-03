import streamlit as st
import openai

openai.api_key = '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'

st.title('GPT-3 sql query generator')
st.markdown('This app generates sql queries using GPT-3 model.')

qurey = st.text_input('Enter your phrase:Create a SQL request to find all users who live in California and have over 1000 credits:')
if st.button('Generate'):
    response = openai.Completion.create(
    model="text-davinci-002",
    prompt=qurey,
    temperature=0.3,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )


    st.text(response.choices[0].text)



