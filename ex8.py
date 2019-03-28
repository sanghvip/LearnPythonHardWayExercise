formatter = "%r %r %r %r"#%r gives the raw representation of the variable to be printed.
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))#output:'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'[1]
print(formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
))

'''
[1]The output contains many %r because while printing we are passing the formatter variable to variable before the %.Moreover the formatter is then referring to '%r %r %r %r'.So in place of each %r formatter var value i.e '%r %r %r %r' will be printed .Hence we have 16 %r.
'''