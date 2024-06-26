import time


# Decorator: counts the number of calls to the LLM, and stops the calls if LLM is called more than 500 times in a single execution.
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        if wrapper.calls > 500:
            raise Exception("Exceded 500 calls to the LLM")
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        print(f"Execution time of {func.__name__}: {time.perf_counter_ns() - start} nanoseconds")
        return result

    return wrapper


