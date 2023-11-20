from langchain.schema import AIMessage
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI


#mission,process,worldview,task,useful_infos='', context_lenght=8000
def context_memory_management():
    """
    in context memory management that uses RAG from the worldview+summarization to fit all useful info in the context lenght
    """
    text = "What do you think about Pisa?"
    llm = OpenAI()

    llm.invoke(text)




def determine_whether_user_input_is_required():
    """
    determine whether user input is required and returns a boolean
    """
    pass

def update_world_model():
    """
    update world model
    """
    pass

def update_working_memory(instruction,working_memory,world_model):
    """
    update working memory
    """
    #1)generate the new tasks required to fulfill the given instruction.

    #2)add the new tasks to the working memory

    #3)reflect upon current tasks, generate thoughts about them, decide whether to change them, and update thoughts

