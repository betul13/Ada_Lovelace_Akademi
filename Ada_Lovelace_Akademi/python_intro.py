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

#fonksiyonlar değer döndürür ve bu değeri return edersek fonksiyon dışında da kullanabiliriz.

def add_two_numbers(number_one, number_two):
  total = number_one + number_two
  return total

add_two_numbers(3,7)

# method ve fonksiyon farkı, methodlarla sınıflar içinde işlem yaparız bu yüzden . ile, fonksiyonlar ise parantezle kullanılır.

text = "Ada Lovelace Academy"
print(type(text))

str.upper(text)

import math
math.pow(2,4)

"""This is a comment """
example_string = "This is a comment" #variable definition

#Docstring

def my_pow(number_one, number_two):
    """
    :param number_one: int, girilmesi gereken ilk değişken
    :param number_two: int, girilmesi gereken ikinci değişken
    :return: int, birinci sayının ikinci sayı kuvvetini döndürür
    """
    result = number_one ** number_two
    return result

my_pow.__doc__

