#!/bin/python3

#for loops

primes = [2, 3, 5, 7, 11, 13, 17]

for prime in primes:
    print(prime)


#Now well play with the range() command
print("\n\n Playing with range(5)")
for x in range(5):
    print(x)

print("\nrange(3,6)")
for x in range(3,6):
    print(x)

print ("\n Lets print out even numbers using range(2,20,2)")
print ("Notice how the first digit includes the index specified, but the second integer EXCLUDES the index specified!")

for x in range(2,20,2):
    print(x)

#Now time to play with while loops
print("\n\nNow it's time for while loops!")

count = 0
while count <= 10:
    print(count)
    count += 1 #same as count = count + 1

#Time to initiate a break in the while loop
print("\n\nUsing the break command in a while loop")

count = 0
while True:
    print(count)
    count += 1
    if count > 10:
        print("count variable has exceeded 10!!")
        break
print("\n\nLets print only Odd numbers")
for x in range(30):
    #here we check if x is even
    if x % 2 == 0: #if x divided by two has a remainded or 0, we have an even number!
        continue
    print(x)

