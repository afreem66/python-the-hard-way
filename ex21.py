def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

print("lets do some math with just functions")

age = add(20, 6)
height = subtract(80, 5)
weight = multiply(100, 2)
iq = divide(100, 100)

print(f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}")

print("Here is a puzzle for extra credit")

what_is = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"that becomes:  {what_is}. Can you do it by hand?")
