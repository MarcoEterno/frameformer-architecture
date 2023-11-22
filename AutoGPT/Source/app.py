import os
from apikey import API_KEY as apikey
from routines import *  # to substitute with specific routines we are using
from prompts import QA_format
from utils import count_calls
from working_memory import WorkingMemory

import os
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

os.environ["OPENAI_API_KEY"] = apikey


@count_calls
def OpenAI_count_calls(*args, **kwargs):
    return OpenAI(*args, **kwargs)


default_llm = OpenAI_count_calls(temperature=0.9, model="gpt-3.5-turbo-instruct")

# App framework
st.title("AutoGPT")

# initialize the components
working_memory = WorkingMemory()

# generate first task list

# generate first thought

# organize


process_is_running = True
while process_is_running:
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

    # 4) stop the execution when there are no tasks left
    if working_memory.tasks == []:
        process_is_running = False

"""
Let's recap the main steps of the process:
1) AGI awakens, and starts to decompose the mission in tasks
2) AGI prioritises the tasks based on temporal dependency (some tasks require input from other tasks)
   3) AGI execute single tasks using this strategy:\
       a) AGI asks itself if the task needs further decomposition(if it does, decomposes the task in subtasks)\
       b) AGI asks itself if the task needs further information from the user (if it does, asks the user for the info)\
       c) AGI generates possible routes to solve the problem\
       d) AGI does a depth-first search, prioritizing the routes most likely to fulfill the task,
          A maximum depth is set, in order to avoid excessive decomposition.\
       e) every time AGI encounters a new fact, it challenges it using the epistemological method (explained below) 
   and if it is true it is added to world model.\
       f) when a solution to the task is proposed, AGI asks itself if the solution is correct (if it is, the task is marked
        as completed)\
       g) the working memory will contain informations about all the open and closed tasks.
4) AGI stops when there are no tasks left.
5) Last step is to paste together the tasks and their answers in the context window, and ask AGI to print to user the 
answer to the mission.

"""
