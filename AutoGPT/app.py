import osfrom apikey import API_KEY as apikey
from routines import * #to substitute with specific routines we are using
from prompts import QA_format

import os
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
    # 1) fetch user input
    model_question = "abc"
    user_input = st.text_input("Answer", "You should do that")
    # x = default_llm(prompt=user_input)
    if user_input != "":
        # update model state by putting user_input in the context window
        new_info = QA_format(model_question, user_input)
    # 2) update the state of the system based on the user input, and execute next task

    # 3) return output to screen if user input is required
    model_output = ""
    st.write(model_output)

    # 4) stp the execution when there are no tasks left
    if(True):
        process_is_running = False


