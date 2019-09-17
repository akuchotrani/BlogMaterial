import time

def calculate_square(data):
    result = []
    start = time.time()
    for number in data:
        answer = number*number
        result.append(answer)
    end = time.time()
    print("Total time it took to execute: "+str((end-start)*1000)+" milliseconds")
    return answer



def calculate_cube(data):
    start = time.time()
    result = []
    for number in data:
        answer = number*number*number
        result.append(answer)
    end = time.time()
    print("Total time it took to execute: "+str((end-start)*1000)+" milliseconds")
    return answer


data = range(1,10000)
calculate_square(data)
calculate_cube(data)
