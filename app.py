# Q&A chatbot

from langchain.llms.openai import OpenAI
from dotenv import load_dotenv
load_dotenv() # take env variable from .env
import streamlit as st
import os


# function to load openai model and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name='gpt-3.5-turbo-instruct',temperature=0.6)
    response=llm(question)
    return response

# initialize streamlit
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input=st.text_input("Ask a question: ",key='input')
response=get_openai_response(input)

submit=st.button("Submit")

if submit:
    st.subheader("The Response is")
    st.write(response)