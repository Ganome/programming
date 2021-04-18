#!/bin/python3


def first_function():
    print("Hello World")
    print("From inside a funtion")

first_function()


def second_function(name, age):
    print("Hello %s, You're getting kind of old at %d. Don't you think?" % (name,age))
    return name + str(age)

second_function("John", 35)


#******COPIED FROM THE WEBSITE***
print("\n\nEverything from here down was copied and pasted from website!!")
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)
