firstInt = input("Enter first number to add:")
secondInt = input("Enter second number to add:")
arithmeticComment = "I have to wrap the 'finalAsnwer' variable inside the int() function, otherwise the integers are treated as strings!"

finalAnswer =int(firstInt) + int(secondInt)
wrongFinalAnswer = firstInt + secondInt

print(firstInt, "+", secondInt, "=", finalAnswer)
print(arithmeticComment)
print("An example of not using the int() function")
print(wrongFinalAnswer)
