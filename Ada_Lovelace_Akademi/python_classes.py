#CLASSES
class MyClass:
    pass #boş geçmek istersek pass yazabiliriz. Bu işlemi fonksiyonlarda da yazabiliriz.


class Animal:
    isalive = True
    age = 0
my_cat = Animal()
my_cat.isalive

Animal.isalive = False

Animal.isalive = True

class Cat:
    salive = True
    age = 0
    sound = "meow"
    def __init__(self, location):
        self.location = location
    def aged(self):
        Cat.age +=1

boncuk = Cat(location = "Home")
boncuk.aged()

#packing and unpacking

fruits = ["apple","banana","cherry","orange"]
first, *remaining, last = fruits
print(remaining)

def my_example(my_number,*args): # my_number daha önce yazılmalı daha sonrasına yazamayız.
    return f"my number is : {my_number}, {args}"
my_example(10,235,487654,5976)

def second_example(**kwargs):
    return kwargs
second_example(number_first_number=10, number_second_number=11,)


def third_example(special_number=1, **kwargs):
    return f"Special number: {special_number}, Others: {kwargs}"
third_example(special_number=2, number_first_number=10, number_second_number=11,)
