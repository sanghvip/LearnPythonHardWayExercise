from datetime import datetime
#Basic Formatting
print('{} {}'.format('one','two'))#output:one two
#Explicit place holder
print('{1} {0}'.format('one','zero'))#output:one zero
#Value conversion
'''print('{:f}'.format("123Hello"))output:one two
zero one
Traceback (most recent call last):
  File "ex5_1.py", line 6, in <module>
    print('{:f}'.format("123Hello"))
ValueError: Unknown format code 'f' for object of type 'str'''
class Data(object):
	first_name='Default_value1'
	last_name='Default_value2'
	type = 'Data'
	def __str__(self):
		return self.first_name
	
	def __repr__(self):
		return 'räpr'

data = Data()
data.first_name = 'Pratik'
data.last_name = 'sanghvi'
print('{0!s} {0!r}'.format(data))#!s is known as a conversion flag
#output for the statement  on line 24
#output:Pratik repr
print('{0!r} {0!a}'.format(data))

#Padding and aligning strings
print('{:_>10}'.format('pratik'))#right align the string with total of ten place holders to represent it.output:____pratik
print('{:_<10}'.format('pratik'))#left align.output:pratik____
print('{:_^10}'.format('pratik'))#output:__pratik__

#Truncating long strings
print('{:.2}'.format('pratik'))#output:pr

#combining truncating and padding
print('{:_^10.2}'.format('pratik'))#output:____pr____

#numbers
print('{:d}'.format(99))#output:99
print('{:.1f}'.format(23.56))#output:23.5
print('{:010.2f}'.format(45.67890))#output:45.68_____.By default the string is right aligned if we do not specify any position.
#signed numbers
print('{: d}'.format(-56))#output:-56
print('{:+d}'.format(56))#output:+56
print('{:5d}'.format((-23)))#output:-23
print('{:_=5d}'.format((-23)))#output:-__23
print('{:_=+5d}'.format(23))#output:+__23

#name place holder
dict1 = {'first_name':'pratik','last_name':'sanghvi'}
print('{first_name} {last_name}'.format(**dict1))#output:pratik sanghvi
print('{first_name} {last_name}'.format(first_name='Pratik',last_name='Sanghvi'))#output:Pratik Sanghvi
print('Type of object of class Data:{p.type}'.format(p=Data()))#output:Type of object of class Data:Data

#Date time
print('{:%Y-%m-%d %H:%M}'.format(datetime(2018, 11, 22, 12, 32)))#output:2018-11-22 12:32

#parameterized formatting
print('{:_{align}{width}}'.format('pratik', align='^', width='10'))#output:__pratik__
print('{:{prec}} = {:{prec}}'.format('Gibberish', 2.7182, prec='.4'))#output:Gibb = 2.718
dt = datetime(2001, 2, 3, 4, 5)
print('{:{dfmt} {tfmt}}'.format(dt, dfmt='%Y-%m-%d', tfmt='%H:%M'))#output:2001-02-03 04:05
print('{:_{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))#output:_____+2.72

class HAL9000(object):

    def __format__(self, format):
        if (format == 'open-the-pod-bay-doors'):
            return "I'm afraid I can't do that."
        return 'HAL 9000'

print('{:open-the-pod-bay-doors}'.format(HAL9000()))#output:I'm afraid I can't do that.
print('{}'.format(HAL9000()))#output:HAL 9000

'''for more detailed explanation refer https://pyformat.info/'''