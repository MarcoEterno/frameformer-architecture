from langchain.schema import AIMessage
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import nltk
import os

# Download the punkt tokenizer (if not already downloaded)
nltk.download('punkt')


def count_tokens(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            tokens = nltk.word_tokenize(text)
            file.close()
            return len(tokens)
    except:
        raise Exception("Error: file not found")


"""
in context memory management that uses RAG from the worldview + summarization to fit all useful info in the context lenght
"""



def summarization_of_infos_relevant_to_task(task, world_model, default_llm, context_lenght=8000):
    """Summarizes useful info"""

    """First step: counting the context length"""
    file_name = 'world_model.txt'
    file_path = os.path.join(os.getcwd(),file_name)
    num_tokens = count_tokens(file_path)

    print(f'Number of tokens in {file_path}: {num_tokens}')  # then comment this line

    """Second step: reads all the world_model and summarizes the relevant info"""
    iterations = num_tokens // context_lenght + 1
    summarization = []

    for i in range(iterations):
        prompt = "YOUR TASK IS: " + task + " READ THIS WORLD MODEL WRITTEN BY YOU AND OUTPUT" + \
                 "ALL THE RELEVANT INFORMATION TO SOLVE THE TASK. YOU ARE NOW SUMMARIZING THE " + str(i) + " / " + \
                 str(iterations) + " PART OF THE WORLD MODEL, WHICH FOLLOWS: " + world_model
        summarization.append(default_llm(prompt) + '\n')

    """Third step"""
    num_summarizations_done = 1
    while count_tokens(summarization) > context_lenght and num_summarizations_done < 3:
        # first argue that the summarization is too long, we define a string, and pass it to the function.
        summarization_of_infos_relevant_to_task(task + "Also: YOU HAVE ALREADY SUMMARIZED THE INFO: BUT IT WAS TOO LONG: " + \
                                                count_tokens(
                                           summarization) + " INSTEAD OF THE CONTEXT LENGTH " + context_lenght + "TRY TO SUMMARIZE IT IN LESS TOKENS!", \
                                                world_model, default_llm)
        num_summarizations_done += 1

    return summarization


def determine_possible_question_to_user():
    """
    determine whether user input is required and returns the question.
    """
    pass
