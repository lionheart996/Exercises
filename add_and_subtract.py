def sum_numbers(a, b):
    return a + b

def subtract(a, b):
    return a - b

def add_and_subtract(*args):
    if len(args) != 3:
        return "Please provide exactly 3 numbers."

    a, b, c = args
    return subtract(sum_numbers(a, b), c)

print(add_and_subtract( 58, 100))

