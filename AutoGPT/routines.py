from langchain.schema import AIMessage
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import nltk

# Download the punkt tokenizer (if not already downloaded)
nltk.download('punkt')

def count_tokens(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        tokens = nltk.word_tokenize(text)
        return len(tokens)



    """
    in context memory management that uses RAG from the worldview + summarization to fit all useful info in the context lenght
    """


#mission,process,worldview,task,useful_infos='', context_lenght=8000
def summarization_of_relevant_info(task, world_model, default_llm):
    """Summarizes useful info"""

    """First step: counting the context length"""
    file_path = 'world_model.txt'  # Change this to the path of your text file
    num_tokens = count_tokens(file_path)
    
    print(f'Number of tokens in {file_path}: {num_tokens}')
    
    """Second step: reads all the world_model and summarizes the relevant info"""
    iterations = num_tokens//context_lenght + 1
    summarization = []

    for i in range(iterations):
        Prompt = "YOUR TASK IS: " + task + " READ THIS WORLD MODEL WRITTEN BY YOU AND OUTPUT" + \
        "ALL THE RELEVANT INFORMATION TO SOLVE THE TASK. YOU ARE NOW SUMMARIZING THE " + i + " / " + \
        iterations + " PART OF THE WORLD MODEL, WHICH FOLLOWS: " + world_model
        summarization.append(default_llm(Prompt))
    
    """Third step"""
    num_summarizations_done = 1
    while count_tokens(summarization) > context_lenght or num_summarizations_done < 3:
        summarization_of_relevant_info(task + "Also: YOU HAVE ALREADY SUMMARIZED THE INFO: BUT IT WAS TOO LONG: " + \
        count_token(summarization) + " INSTEAD OF THE CONTEXT LENGTH " + context_lenght + "TRY TO SUMMARIZE IT IN LESS TOKENS!", \
        world_model, default_llm)
        num_summarizations_done += 1
    
    return summarization


def determine_whether_user_input_is_required():
    """
    determine whether user input is required and returns a boolean
    """
    pass


