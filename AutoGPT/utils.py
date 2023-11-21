# Decorator: counts the number of calls to the LLM, and stops the calls if LLM is called more than 500 times in a single execution.
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# Example of usage
@count_calls
def test_function():
    print("Function is called")

# Calling the function a few times to test
test_function()
test_function()
test_function()

# Printing the total number of calls
print(f"The function was called {test_function.calls} times.")