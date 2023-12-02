import unittest
from unittest.mock import patch
from AutoGPT.source.framework.framework import Framework


class TestFramework(unittest.TestCase):

    #@patch('AutoGPT.source.framework.framework.Framework.test_program_routine')
    def test_test_program_routine(self):
        # Setup mock return value
        #mock_execute.return_value = ("Hello World", "")

        # Create a Framework instance and call test_program_routine
        framework = Framework()
        output, error = framework.test_program_routine("print('Hello World')")

        # Asserts
        self.assertEqual(output, "Hello World")
        self.assertEqual(error, "")

    # ... other test cases for test_program_routine

    #@patch('AutoGPT.source.framework.framework.Framework.determine_optimal_framework_type')
    def test_determine_optimal_framework_type(self):
        # Setup mock OpenAI response
        # mock_openai.return_value = "text"

        # Create a Framework instance and call determine_optimal_framework_type
        framework = Framework()  # fill with necessary initialization parameters
        text_framework = framework.determine_optimal_framework_type(objective="summarize a given sentence")
        program_framework = framework.determine_optimal_framework_type(objective="predict the next chess move given a "
                                                                                 "chess board")

        print(text_framework, program_framework)
        # Assert
        self.assertEqual(text_framework, " text")
        self.assertEqual(program_framework, " program")
        self.assertEqual(framework.id, 1)
        self.assertEqual(framework.name, "")

    # ... other test cases for determine_optimal_framework_type


if __name__ == '__main__':
    unittest.main()
