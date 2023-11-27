# NUMBERS

my_number = 12345

type(my_number)

my_float = 3.14

type(my_float)

print(f"{my_float} tipi floattır")

print(f"{my_float} + {my_number} = " ,my_float + my_number)

6 / 5 #float
6 // 5

#Modulonun başka yolu
whole_part = int(5 / 3)
decimal_part = 5 / 3 - whole_part
print(decimal_part)

whole_remainder = decimal_part * 3
print(whole_remainder)


#Decimal

from decimal import Decimal
Decimal('0.1') * 3

import random
random.randint(0, 99)

#Strings

my_string = 'my text is "important"'
print(my_string)

long_string = '''
 ###
 text
    example
'''
print(long_string)

my_number = 42
my_number = str(my_number)
print(type(my_number))

len(my_string[-1])

my_string.split()


animals = ["cat", "dog", "horse"]

", ".join(animals)

for item in my_string:
    print(item)

#fstrings

name = "Kemal"
age = 33
print(f"My name is {name} and my age is {age}.")


import datetime
today = datetime.datetime.today()
print(today)
print(f"{today:%d %B %Y}")

#Boolean

my_variable = 0
if my_variable:
    print("yes it is true")
else:
    print("no it is false")


my_variable is True