#Get user's string

userString = input("Enter a string to start slicing: ")

num1 = int(input ("Now enter Starting point of the slice: ")) #This technique is known as type-casting!
num2 = int(input ("Now pick where to end the slice: ")) #If you do not enter an integer, the program will crash

print("The string was sliced at: %d & %d" % (num1, num2))
#print(f"The string was sliced at: {num1} & {num2}") #This produces the exact same output as above!

print("Your sliced string:\n", userString[num1:num2+1]) #We have to add 1 to the end because the Start slice is inclusive.  The end slice is EXCLUSIVE!