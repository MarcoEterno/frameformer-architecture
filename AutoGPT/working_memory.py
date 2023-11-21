from collections import deque


class WorkingMemory:

    def __init__(self):
        self.tasks = deque()
        self.thoughts = deque()

    def add_thought(self, thought):
        self.thoughts.append(thought)

    def clear(self):
        self.memory = []

    def add_task(self, task):
        self.tasks.append(task)

    def reorder_tasks_based_on_importance(self):
        # call the llm to get the importance of each task, then reorder the tasks based on it and on the thoughts.
        pass

    def get_next_task(self):
        return self.tasks.popleft()

    def generate_thought_based_on_tasks(self):
        # call the llm to generate a thought based on the tasks
        pass
