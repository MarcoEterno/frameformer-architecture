import os
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ["OPENAI_API_KEY"] = apikey

# App framework
st.title("AutoGPT")
user_prompt = st.text_input("Prompt", "Hello, I am a robot.")

# LLMs
default_llm = OpenAI(temperature=0.9, model = "gpt-3.5-turbo-instruct")


# return output to screen
if user_prompt:
    response = default_llm(prompt=user_prompt)
    st.write(response)


