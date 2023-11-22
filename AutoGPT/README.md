# Thought implementation in LLMs
While LLMs are advancing towards human level intelligence in many fields,
the thought processes that characterize a human are far from being 
implemented in the standard full stack implementations of 
currently available models.

This project aims to implement the thought process in LLMs, 
through the implementation of N distinct contributions:
1. A long term memory
2. A routine to access the long term memory and retrieve only relevant content
3. An organized scientific process through which the world model is updated


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
   statements about the world. This memory is implemented using text, 
   vector databases and knowledge graphs. 
    The world model is updated using the scientific process.
2. **mission**: is the goal of the AI, specified in text in the memory file.
3. **working_memory**: contains the current set of tasks open,
the relevant informations about those tasks, and the current thoughts of the AI.
Tasks and thoughts are implemented using JSON objects.

## History of the agent


3. while doing that, the agent can further decompose the subtasks into 
   sub-subtasks, and each time it discover something about the world it writes
   it on the world model. The process by which the agent does that is a depth-first 
   search, that prioritizes the most relevant subtasks, and prioritizes 
   the most likely ways to fulfill them. a maximum depth is set, in order to avoid
   excessive decomposition.

## History of the agent
Let's recap the main steps of the process:
1) AGI awakens, and starts to decompose the mission in tasks
2) AGI prioritises the tasks based on temporal dependency (some tasks require input from other tasks)
   3) AGI execute single tasks using this strategy:\
       a) AGI asks itself if the task needs further decomposition(if it does, decomposes the task in subtasks)\
       b) AGI asks itself if the task needs further information from the user (if it does, asks the user for the info)\
       c) AGI generates possible routes to solve the problem\
       d) AGI does a depth-first search, prioritizing the routes most likely to fulfill the task,
          A maximum depth is set, in order to avoid excessive decomposition.\
       e) every time AGI encounters a new fact, it challenges it using the epistemological method (explained below) 
   and if it is true it is added to world model.\
       f) when a solution to the task is proposed, AGI asks itself if the solution is correct (if it is, the task is marked
        as completed)\
       g) the working memory will contain informations about all the open and closed tasks.
4) AGI stops when there are no tasks left.
5) Last step is to paste together the tasks and their answers in the context window, and ask AGI to print to user the 
answer to the mission.

## The epistemological method


terminal

So these routines are useful:
1. **decompose**: decomposes a task into subtasks, and adds them to the working memory.
2. **fulfill**: tries to fulfill a task, and if it can't, decomposes it into subtasks.
3. **evaluate_strategies** lists the strategies to fulfill a task, and adds them to the working memory 
   with a score, which is related to the probability that the strategy will work.
4. 


