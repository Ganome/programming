print("Let's practice everything.")
print("You'd need to know about escapes with \\")
print("\n newlines and \ttabs")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-----------")
print(poem)
print("-----------")


five = 10 - 2 + 3 - 6
print(f"this should be five: {five}")

def secretFormula(started):
    jellyBeans = started * 500
    jars = jellyBeans / 1000
    crates = jars / 100
    return jellyBeans, jars, crates


startPoint = 10000
beans, jars, crates = secretFormula(startPoint)

#another way to format a string
print("With a starting point of {}".format(startPoint))
#Identical to the print(f" ") method
print(f"We have {beans} beans, {jars} jars, and {crates} crates.")

startPoint = startPoint / 10

print("We can also do that this way:")
formula = secretFormula(startPoint)
print("We'd have {} beans, {} jars, {} crates".format(*formula))