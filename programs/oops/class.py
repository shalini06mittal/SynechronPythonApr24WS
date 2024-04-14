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
        print('Book init called')
        self.title = title
        self.__description = description
        self.price = price

    # def display(self):
    #     print(self.title, self.description, self.price)
    def display(self):
        
       # print(self)
        print(self.title, self.__description, self.price)


    def getDescription(self):
        return self.__description
    
    def setDescription(self, description):
        self.__description = description

    # def getMRP(self):
    #     mrp = self.price + 0.10 * price
    #     return mrp
    
    def getMRP(self, tax=0.10):
        mrp = self.price + tax * self.price
        return mrp
    
    def __str__(self) -> str:
        print('str')
        return 'Title '+self.title+' Price '+str(self.price)+' Description '+self.__description
# b2 = Book('C',34.56,'Enjoy learning')
# print(b2.getMRP())
# print(b2.getMRP(5))

# b1 = Book('Core Java', 123.89)
# print(b1)
# b1.display()



# b2.__description = ' Learn C Programming '
# print(b2)
# print(b2.__description)
# b2.setDescription( 'Acceslerate your career')
# print(b2)
# print(b2.__description)
# b2.title = 'C programming'
# print(b2)

# b2.display()

# inheritance

class Novel(Book):
    def __init__(self, title, price,pages, description='') -> None:
        print('Novel init')
        super().__init__(title, price, description)
        self.pages = pages
    def __str__(self) -> str:
        return super().__str__() + 'Pages '+str(self.pages)

class Academic(Book):
    def __init__(self, title, price,branch, description='') -> None:
        super().__init__(title, price, description)
        self.branch = branch


    
n1 = Novel('HTML',100,100)
print(n1)