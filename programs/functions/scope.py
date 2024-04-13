# int str float tuples are immutable
# nonlocal - nested functions
x=10
def f1():
    #global x
    # print('1',x)
    x = x+ 100
    print('4',x)

# print('2',x)
# f1()
# x=x+10
# print('3',x)

l1=[1,2,3]
def f2():
    print('f1 called')
    # print(l1)
    # l1.append(10)
    # print(l1)
    l1=l1+[4,5,6]
    print(l1)
    print('f1 end')
print('1', l1)
f2()
print(2, l1)

