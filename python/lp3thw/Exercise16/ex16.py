from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you want to cancel, HIT CTRL-C (^C) NOW!!!")
print("If you want to proceed, hit Enter")

input("?")

print(f"Opening the file...{filename}")
target = open(filename, 'a')
#https://docs.python.org/3/library/functions.html#open documentation on open()

#print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you a write a few lines: ")

Q1 = input("Line 1: ")
Q2 = input("Line 2: ")
Q3 = input("Line 3: ")

print(f"Now I'll write the 3 lines to {filename}")

allQ = Q1 + "\n" + Q2 + "\n" + Q3 + "\n"
target.write(allQ)
#target.write("\n")
#target.write(Q2)
#target.write("\n")
#target.write(Q3)
#target.write("\n")

print(f"Finished writing, closing {filename}.")
target.close()
