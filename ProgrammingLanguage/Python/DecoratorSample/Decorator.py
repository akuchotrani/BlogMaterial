import time

def function_runtime_decorator(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ + " took "+ str((end-start)*1000) + " milliseconds");
    return wrapper


@function_runtime_decorator
def calculate_square(data):
    result = []
    for number in data:
        answer = number*number
        result.append(answer)
    return result

@function_runtime_decorator
def calculate_cube(data):
    result = []
    for number in data:
        answer = number*number*number
        result.append(answer)
    return result


data = range(1,10000)
calculate_square(data)
calculate_cube(data)
