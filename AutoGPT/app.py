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
user_prompt = st.text_input("Prompt", "Hello, I am a robot.")

model_response = default_llm(prompt=user_prompt)

# return output to screen
if model_response:
    st.write(model_response)

process_is_running = True
while (process_is_running):
    # 1) fetch user input
    user_input = st.text_input("Prompt", "Solve world hunger")

    # 2) update the state of the system based on the user input, and execute next task

    # 3) return output to screen if user input is required
