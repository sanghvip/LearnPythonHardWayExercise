print("Mary had a little lamb")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6,end=" ")
print(end7 + end8 + end9 + end10 + end11 + end12)

#Example of using end with format()
print("Pratik {}".format("sanghvi"),end="@")#Output:Pratik Sanghvi@

''' 
In python 3 print by default ends the line with \n.So the next print statement will start on a new line.To print on the same line use the 'end' attribute and specify the value.
'''