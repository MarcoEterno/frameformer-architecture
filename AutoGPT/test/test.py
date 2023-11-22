import unittest

import os
from apikey import API_KEY as apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from routines import summarization_of_infos_relevant_to_task

def open_file_get_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            file.close()
            return text
    except:
        raise Exception("Error: file not found")

def user_confirmation(answer):
    user_input = input(f"Is the answer {answer} correct? Press Y or N for yes or no: ")
    return user_input.lower() == 'y'

class Test_summarization_of_infos_relevant_to_task(unittest.TestCase):
    def test_of_summarization(self):
        os.environ["OPENAI_API_KEY"] = apikey
        default_llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")
        
        task = "Which creatures and which men do Dante see in the wilds?"
        divine_comedy_chapter_one = open_file_get_text("AutoGPT/divine_comedy_chapter_one.txt")
        answer = summarization_of_infos_relevant_to_task(task, divine_comedy_chapter_one, default_llm, 80)
        print(answer)

        # Ask for user confirmation
        confirmation_result = user_confirmation(result)

        # Assert that the user confirmed the correct answer
        self.assertTrue(confirmation_result)

if __name__ == '__main__':
    unittest.main()
