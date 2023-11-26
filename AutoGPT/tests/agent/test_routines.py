import unittest

import os
from AutoGPT.source.root.apikey import API_KEY as apikey
from langchain.llms import OpenAI
from AutoGPT.source.agent.routines import summarize_infos_relevant_to_task
from AutoGPT.source.agent.routines import give_answer

os.environ["OPENAI_API_KEY"] = apikey

def open_file_get_text(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            file.close()
            return text
    except:
        raise Exception("Error: file not found")

def ask_user_for_confirmation(answer):
    user_input = input(f"Is the answer {answer} correct? Press Y or N for yes or no: ")
    return user_input.lower() == 'y'

class Test_summarization_of_infos_relevant_to_task(unittest.TestCase):
    def test_of_summarization(self):
        """
        Test of the summarization of infos relevant to a task.
        It only runs if executed with the -s flag, in order to capture user confirmation
        """
        default_llm = OpenAI(temperature=0.9, model="gpt-3.5-turbo-instruct")
        
        task = "Which creatures and which men do Dante see in the wilds?"

        file_path = os.path.join(os.path.dirname(__file__), "divine_comedy_chapter_one.txt")
        divine_comedy_chapter_one = open_file_get_text(file_path)
        relevant_info = summarize_infos_relevant_to_task(task, divine_comedy_chapter_one, default_llm, 800)
        answer = give_answer(task, relevant_info, default_llm, 8000)

        # Ask for user confirmation
        confirmation_result = ask_user_for_confirmation(answer)

        # Assert that the user confirmed the correct answer
        self.assertTrue(confirmation_result)

if __name__ == '__main__':
    unittest.main()
