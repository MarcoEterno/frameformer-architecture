class WorkingMemory:
    def __init__(self, memory_size):
        self.tasks = memory_size
        self.memory = []

    def add(self, item):
        self.memory.append(item)
        if len(self.memory) > self.memory_size:
            self.memory.pop(0)

    def get(self):
        return self.memory

    def clear(self):
        self.memory = []