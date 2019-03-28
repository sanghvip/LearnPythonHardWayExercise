ten_things = "Apples Oranges Crows Telephones Light Sugar"

print("Wait theres not 10 things on list lest fix that")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print("Adding:{}".format(next_one))
	stuff.append(next_one)
	print("Theres {} many items now".format(len(stuff)))
	
print("There we go {}".format(stuff))

print("Lets do something with stuff")

print(stuff[1])

print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))