from sys import argv

script, first, second, third = argv
print(type(argv))#output:<class 'list'>
print("The script is called:{}".format(first))
print("Your first variable is:{}".format(second))
print("Your second variable is:{}".format(third))
first = input("Enter value for first variable:")
