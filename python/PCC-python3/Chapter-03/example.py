# Introduction to Python Programming
# Lesson 03 Assignment
# Sample Solution

# Please note that this program takes advantage of the fact that
#   once a condition is met, the if structure is exited.  This
#   allows me to not need a lower limit in my conditions because
#   if the speed were below the minimum for that Category, the
#   program would have already printed the result and exited.

speed = eval(input("Please enter the wind speed: "))

if speed < 74:
    print ("This is not a hurricane")
elif speed <= 95:
    print ("Category 1")
elif speed <= 110:
    print ("Category 2")
elif speed <= 130:
    print ("Category 3")
elif speed <= 155:
    print ("Category 4")
else:
    print ("Category 5")


