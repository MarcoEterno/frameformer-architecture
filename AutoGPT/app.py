import os
from apikey import apikey
from routines import * #to substitute with specific routines we are using

os.environ['OPENAI_API_KEY'] = apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ["OPENAI_API_KEY"] = apikey
default_llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")

# App framework
st.title("AutoGPT")

process_is_running = True
while (process_is_running):
    #1) get user input if present
    user_prompt = st.text_input("Prompt", "solve world hunger")

   #updating the internal state of the system, and generating output for the user when needed.

    model_response = default_llm(prompt=user_prompt)
    st.write(model_response)

