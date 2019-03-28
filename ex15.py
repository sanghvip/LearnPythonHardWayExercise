from sys import argv

script, filename = argv
print("Script name:{}".format(script))

txt = open(filename)#by default which mode

print("Return value from file:{}".format(type(txt)))

print("Heres your file".format(filename))

print(txt.read())

close(txt)

print("Type the filename again")

file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

close(txt_again)