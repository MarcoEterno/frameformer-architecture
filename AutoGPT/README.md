# Thought implementation in LLMs
While LLMs are advancing towards human level intelligence in many fields,
the thought processes that characterize a human are far from being 
implemented in the standard full stack implementations of 
currently available models.

This project aims to implement the thought process in LLMs, 
through the implementation of N distinct contributions:
1. A long term memory
2. A routine to access the long term memory and retrieve only relevant content
3. an organized scientific process through which the world model is updated


## Memory implementation
Different types and architectures of memory are implemented.  
### Architectures
The 3 different **architectures** of memory used are:
1. Text based memory
2. Vector database
3. Knowledge graph

### Memory types
The different types of memory used are:
1. **world_model**: a file containing the world model, which is a set of 
   statements about the world. this memory is implemented using text, 
   vector databases and knowledge graphs. 
    The world model is updated using the scientific process.
2. **mission**: is the goal of the AI, specified in text in the memory file.
3. **working_memory**: contains the current set of tasks open,
the relevant informations about those tasks, and the current thoughts of the AI.
Tasks and thoughts are implemented using JSON objects.

## History of the agent

1. The agent is initialized with a mission, and should try to fulfill it. 
2. The agent should first try to decompose the mission into subtasks, 
   and then try to fulfill those subtasks.
3. while doing that, the agent can further decompose the subtasks into 
   sub-subtasks, and each time it discover something about the world it writes
   it on the world model




