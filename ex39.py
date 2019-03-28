states = {'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}

cities ={
'CA':'San Francisco',
'MI':'Detroit',
'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('_'*10)
print("NY state has:{}".format(cities['NY']))
print("OR state has:{}".format(cities['OR']))

#print some states
print("_"*10)
print("Michigan  abbrevation is:{} ".format(states['Michigan']))
print("Florida abbreciation is: {}".format(states['Florida']))

print('_' * 10)
print('Michigan has:{}'.format(cities[states['Michigan']]))
print('Florida has:{}'.format(cities[states['Florida']]))

print('_'*10)
print(states.items())
for state, abbrev in states.items():
	print("{} is abbreviated {}".format(state,abbrev))

print("_"*10)
for abbrev, city in cities.items():
	print("{} has the city {}".format(abbrev,city))
	
print("_"*10)
for state, abbrev in states.items():
	print("{} state is abbreviated {} and has city {}".format(state,abbrev,cities[abbrev]))
	
print("_"*10)
state = states.get('Texas', None)

if (not state):
	print("Sorry, no texas")
	
city = cities.get('TX','Does not exists')
print("The city for the state 'TX' is: {}".format(city))


#print("{} is abrevated as {}".format(state,abbrev))