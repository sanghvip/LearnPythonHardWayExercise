#using global key word

x= 1

def func1():
	global x
	x+=1
	assert (x<4),"Value of x:{}".format(x)
	
def func2():
	global x
	assert (x<4),"Value of x:{}".format(x)
	x+=1
	
func1()
func2()

print("Value of X:{}".format(x))

#using yield for returning generator

def mygenerator():
	myList = range(3)
	
	for i in myList:
		yield i*i
		
gen = mygenerator()

for i in gen:
	print(i)
	
#using exec in python
exec('x=2+3+4\nprint(x)')

add = lambda x : pow(x,2)
print(add(3))
#https://medium.com/@happymishra66/lambda-map-and-filter-in-python-4935f248593

flt = 1.23
print()
print(type(flt))

longVar = 123
print()
print(type(longVar))

x = add

@add
def myFunc():
	x(5)