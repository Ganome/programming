typesOfPeople = 10
x = f"There are {typesOfPeople} types of people"

binary = "binary"
doNot = "don't"
y = f"Those who know {binary} and those who {doNot}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'") #notice that we can wrap our {} variable in quotes and they still work

hilarious = False
jokeEvaluation = "Isn't that joke so funny! {}"
print(jokeEvaluation.format(hilarious))

w = "This is the left side of ..."
e = "A string with a right side."

print(w + e)
