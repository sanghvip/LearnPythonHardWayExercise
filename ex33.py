
	
def loopOver(testVar,increments):
	i = 0
	numbers = []	
	while(i < testVar):
		print("At the top i is {}".format(i))
		numbers.append(i)
		i = i + increments
		print("Numbers now: ", numbers)
		print("At the bottom i is {}".format(i))
		print ("The numbers: ",end=" ")
		for num in numbers:
			print(num,end=" ")
		print("\n")
		
loopOver(12,2)

elements = [x for x in range(0,12,2)]

print("Elements:{}".format(elements))