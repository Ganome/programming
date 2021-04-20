#!/usr/bin/python3
i = 0
numbers = []

while i <= 5:
    print(f"At the top i is {i}")
    numbers.append(i)

    i += 1
    print(f"Numbers now: {numbers}")
    print(f"At the bottom is: {i}")


print("The numbers: ")

for num in numbers:
    print(num)