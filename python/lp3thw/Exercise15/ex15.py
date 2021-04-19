from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}")
print(txt.read())

print("Type the filename again: ")
fileAgain = input("> ")

txtAgain = open(fileAgain)

print(txtAgain.read())
#It seems that you can only have one active file stream open at a time.  So in order to print the txt variable, we would need to redefine it.
#txt = open(filename)
#print(txt.read())
