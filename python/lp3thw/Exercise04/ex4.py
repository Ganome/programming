cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are %d cars available" %cars)
print("There are only %d drivers available" %drivers)
print("There will be %d empty cars today" %cars_not_driven)
print("We can transport %.1f people today" %carpool_capacity)
print("We have %d to carpool today" %passengers)
print("We have to put about %.1f in each car" %average_passengers_per_car)
