no = 2# 1 to 20
'''
1 2 3 4
2 4 6 8
3
4
5..
10
'''
for no in range(1,11):
    for i in range(1,11):
        print(no*i)


a=1
for i in range(2):
    for b in range(2):
        a=a+b
print(a)

for i in range(2):
    a=1
    for b in range(2):
        a=a+b
print(a)

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            break
        print(i,j)
