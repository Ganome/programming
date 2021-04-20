#!/usr/bin/python3
states = {
    'Oregon' : 'OR',
    'Colorado' : 'CO',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}

cities = {
    'CA' : 'San Jose',
    'CA' : 'Sacramento',
    'CO' : 'Denver',
    'CO' : 'Colorado Springs',
    'MI' : 'Detroit',
    'NY' : 'New York City',
    'FL' : 'Jacksonville',
    'OR' : 'Portland'
}

print('-' * 10)
print("NY State has: ", cities['NY'])
print(f"Colorado state has: {cities['CO']}")

print("-" * 10)
print("Michigan's Abbrviation is: ", states['Michigan'])
print(f"California's abbreviation is: {states['California']}")

print("Colorado has city: ", cities[states['Colorado']])
print(f"Florida has city: {cities[states['Florida']]}")

print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has abbreviation {abbrev}")

#print every city in every state
for city, state in list(cities.items()):
    print(f"{city} has {state}")

#now both at the same time!
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#safely fetch a state from the list that does not exist

state = states.get("Texas")

if not state:
    print(f"Sorry that state is not in our list!")

#get a city with default value
city = cities.get("TX", "Does not Exist")
print(f"The city for the state 'TX' is: {city}")