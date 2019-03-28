def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print("You have {} cheese".format(cheese_count))
	print("you have {} boxes of crackers!".format(boxes_of_crackers))
	print("Man thats enough for a party")
	print("Get a blanket")
	
print("We can just give the function numbers directly:")
cheese_and_crackers(20,300)

print("Or we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can do the math inside too")
cheese_and_crackers(10+20,5+6)

print("And we can combine the 2 variables and math")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)

def whoami(name):
	print("My name is {}".format(name))
	
whoami("pratik")

name = input("Enter your name>")
whoami(name)

whoami("p"+"r"+"a"+"t"+"i"+"k")
