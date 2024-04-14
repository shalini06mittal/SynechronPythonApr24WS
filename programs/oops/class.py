'''
class allows you to bind all the data and members together.
Priniciples of OOPS:
1. abstraction: hides the complexity or business logic or implementation details
2. encapsulation: binding all data and members together within a block: class
access specifier : private, public, protected
package them
3. polymorphism: static/compile-time -> method overloading [ not supported ]
dynamic/run-time -> method overriding [ supported ]
4. inheritance: resusability but at the same time extend and provide custom functinalities as well
'''
# CRUD => Book : title author price description
title =''
author =''
description =''
price = 0 # global
def getMRP():
    global price
    mrp = price + 0.10 * price
    return mrp

# b1 .... B100
class Book:
    # self = this
    def __init__(self, title, price, description='') -> None: # constructor
       # print('init called',self)
        self.title = title
        self.__description = description
        self.price = price

    # def display(self):
    #     print(self.title, self.description, self.price)
    def display(self):
        
       # print(self)
        print(self.title, self.__description, self.price)


    def setDescription(self, description):
        self.__description = description

    def __str__(self) -> str:
        print('str')
        return 'Title '+self.title+' Price '+str(self.price)+' Description '+self.__description

# b1 = Book('Core Java', 123.89)
# print(b1)
# b1.display()
b2 = Book('C',34.56,'Enjoy learning')
b2.__description = ' Learn C Programming '
print(b2)
print(b2.__description)
b2.setDescription( 'Acceslerate your career')
print(b2)
print(b2.__description)
b2.title = 'C programming'
print(b2)

# b2.display()