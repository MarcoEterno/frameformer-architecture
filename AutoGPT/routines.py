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


