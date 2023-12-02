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

## Boolean operators
#on, or, not

not True and True

result = 1 and 0
bool(result)

True or False

first_number = 5
second_number = 55

if first_number > second_number:
    print(f"{first_number} is greater than {second_number}")
elif first_number == second_number:
    print(f"{first_number} is equal {second_number}")
else :
    print(f"{second_number} is greater than {first_number}")

test_score = 80
age = 18

def driver_status(age, test_score):
    if  (test_score >= 80):
        if 18 > age >=16:
            return "intern-driver"
        elif age >= 18:
            return "driver"
    elif 80 > test_score >= 60:
        if 18 > age >=16:
            return "supervised_intern_driver"
        elif age >= 18:
            return "supervised_driver"
    else:
        return "no license"

def buzz_func(number):
    return "Buzz!" if number % 2 == 0 else str(number)
buzz_func(12)

#String Methods

test_string = "         Ada Lovelace Academy had started!"
test_string.strip()
test_string.endswith("!")
test_string.replace("!",".")

#comparisons
15 != 10
first_number = 14

list_1 = [12,34,1,3,4]
3 in list_1

## List

example_list = ["string",[1,2,3],1]
test_list = list("string")

for index, value in enumerate(test_list,1):
    print(f"{index} : {value}")

cubes_to_1000 = [i**3 for i in range(1000)]
print(cubes_to_1000)
example_list.pop()
new_list = cubes_to_1000.copy()
new_list.append(12)
new_list.insert(2,1234567)

#extend
example_list.extend(cubes_to_1000)
cubes_to_1000.sort(reverse = True)

#tuples #immutable

my_tuple = tuple()
my_tuple = tuple([10])
tuple_1 = (12,456,46,6890,78)
listem = [i for i in enumerate(tuple_1)]

#dict
animal_colors_tuple = {"cat":"yellow","dog":"black"}
tuple_2 = tuple(animal_colors_tuple.items())

animals = {"cat" : {"color":"orange", #sıralı değillerdir
                    "age":4},
           "dog":{"color":"black",
                    "age":5}}

animals.get("cat") # get ile çağırdığımızda sözlükde bu anahtar olmasa dahi hata döndürmez

animals["bear"] = {"color":"brown",
                  "age": "12"}

animals.pop("bear")

for animal,knowledge in animals.items() :
    print(f"{animal} : {knowledge}")
