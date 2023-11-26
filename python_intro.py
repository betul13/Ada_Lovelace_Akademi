#VARİABLE

first_variable = 30

print(type(first_variable))

print(first_variable)

first_variable = "Ada Lovelace Akademi"

print(first_variable)

#Collections

import collections
first_variable = collections.Counter([1,1,2,2,3,4,4,4])
print(type(first_variable))
print(first_variable)

#Constants

MY_CONSTANT = 15 #bu değer değiştirilmez, değiştirilmemesi önerilir.
#MY_CONSTANT = 30  başka değer atanabilir ancak önerilmez.

#Functions

def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  print(total)

add_two_numbers(4, 5)

add_two_numbers(1,3)