# resusable block of code
# datetime
def greet():
    print('Good morning')


def greet(name):
    print('Good evening',name)

# greet()
# print(greet('shalini'))

def add(a,b):
    return a+b

# print(add(2,4))

def squares(no):
    return no**2

def calculate(data, f): # f = squares
    print(f)
    print([f(d) for d in data])
    # for d in data:
    #     print(f(d))

n1 = [1,2,3,3,45,6,7,8,9]
calculate(n1, squares)




    
