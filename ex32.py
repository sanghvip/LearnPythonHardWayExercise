the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print("This is count {}".format( number))

for fruit in fruits:
	print("A fruit of type: {}".format(fruit))

for i in change:
	print ("I got {}".format(i))
	
elements = []

for i in range(0,6):
	print("Adding {} to the list".format(i))
	elements.append(i)
	
for i in elements:
	print("Element was: {}".format(i))
	
#avoiding for loop and using generators
elements1 = [x for x in range(0,6)]

print(elements1)
	
