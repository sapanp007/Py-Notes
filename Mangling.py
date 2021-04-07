"""obj._class__var"""

"""
__leading_double_underscore
Leading double underscore tell python interpreter to rewrite name in order to avoid conflict in subclass.
Interpreter changes variable name with class extension and that feature known as the Mangling.
testFile.py
"""


class Myclass():
    def __init__(self):
        self.__variable = 10


"""
>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.__variable
Traceback (most recent call last):
File "", line 1, in
AttributeError: Myclass instance has no attribute '__variable'
nce has no attribute 'Myclass'
>>> obj._Myclass__variable
10
"""

"""
In Mangling python interpreter modify variable name with ___.
 So Multiple time It use as the Private member because another class can not access that variable directly. 
 Main purpose for __ is to use variable/method in class 
 only If you want to use it outside of the class you can make public api
"""


class Myclass():
    def __init__(self):
        self.__variable = 10

    def func(self):
        print(self.__variable)


"""
Calling from Interpreter

>>> import testFile
>>> obj = testFile.Myclass()
>>> obj.func()
10
"""

"""Example to update __ variable"""


class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

# change the price
c._Computer__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
