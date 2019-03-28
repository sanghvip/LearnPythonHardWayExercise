## Animal is- a object (yes, sort of confusing) look at the extra credit
2 class Animal(object):
3 pass
4
5 Dog is a animal
6 class Dog(Animal):
7
8 def __init__(self, name):
9 ##Dog has a name
10 self.name = name
11
12 ## cat is a animal
13 class Cat(Animal):
14
15 def __init__(self, name):
16 ##init has a name
17 self.name = name
18
19 ## Person is a object
20 class Person(object):
21
22 def __init__(self, name):
23 ## Person has a name 
24 self.name = name
25
26 ## Person has- a pet of some kind
27 self.pet = None
28
29 ## Employee is a person
30 class Employee(Person):
31
32 def __init__(self, name, salary):
33 ## ?? hmm what is this strange magic?
##Employee has a name
34 super(Employee, self).__init__(name)
35 ## Employee has a salary
36 self.salary = salary
37
38 ## Fish is a object
39 class Fish(object):
40 pass
41
42 ## Salmon is a fish
43 class Salmon(Fish):
44 pass
45
46 ## ?Halibut is a fish
47 class Halibut(Fish):
48 pass
49
50
51 ## rover is- a Dog
52 rover = Dog("Rover")
53
54 ## satan is a cat
55 satan = Cat("Satan")
56
57 ## mary is a Person
58 mary = Person("Mary")
59
60 ## mary has a pet who is satan
61 mary.pet = satan
62
63 ## Frank is a Employee with name frank and salary 120000
64 frank = Employee("Frank", 120000)
65
66 ## frank has a pet which is a rover
67 frank.pet = rover
68
69 ## flipper is a Fish
70 flipper = Fish()
71
72 ## crouse is a Salmon
73 crouse = Salmon()
74
75 ## harry is a Halibut
76 harry = Halibut()