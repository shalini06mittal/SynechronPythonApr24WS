# Creation of tuple
t1 = 2,3,4,5,2,3,7,8,9,2
print(type(t1))
t2 = (2,)
print(type(t2))
t3=tuple('aeiou')
print(t3)
print('a' in t3)
print('f' in t3)
print(len(t3))

print(sum(t1))
print(max(t1))
print(min(t1))

print(max(t3))
print(t1.count(2))
print(t1[3])
print(t1[4:])
# t1[0] = 100

t1="hey"
print(t1)
print(t3)
del t3
# print(t3)
n1 = 2,4,6,8

# print(all(ele %2==0 for ele in n1))

n2=2,3,4,-1,5
print(all(n2))
print(all(n1))
a = 0
if a:
    pass

t4=(1,2,3,(5,6,7),8)
print(len(t4))
# to access 6
print(t4[3][1])

# operations

t1=1,2,3
t2=3,4
print(t1+t2)
print(t1)
print(t2)
print(t1*3)
# unpack
a,b = t1
print(a,b)



