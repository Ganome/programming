theCount = [1, 2, 3, 4, 5]
fruits = ["Apples", "Oranges", "Pears", "Apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

#this for loop will iterate though a list
for number in theCount:
    print(f"this is count {number}")

#This for loop does the same as above, with a different variable name
for fruit in fruits:
    print(f"This is a(n): {fruit}")

#also we can go through mixed lists too
#notice we have to use {} since we dont know what's in it - copied from book and doesn't make sense
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6): #NOTE that the last digit in range is EXCLUSIVE. not Inclusive.   Meaning it is not included!
    print(f"Adding {i} to the list")
    #append is a list function
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")

