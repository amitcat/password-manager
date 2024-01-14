#run the code and check the output
#find the mistake in the code using the debugger and fix it so the outcome will be correct
def addition(a, b):
    result = a + b
    return result


def multiplication(a, b):
    result = a * b
    return result


def division(a, b):
    result = a / b
    return result


print("((5+2)x10)/2 is", division(multiplication(addition(5, 2), 10), 2))
