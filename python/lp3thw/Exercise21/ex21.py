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
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!!")

age = add(30, 5)
height = subtract(75, 3)
weight = multiply(60, 3)
iq = divide(200, 2)

print(f"Age: {age} \nHeight: {height} \nWeight: {weight} \nIQ: {iq}")

#extra credit
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"The what variable is equal to: {what}")