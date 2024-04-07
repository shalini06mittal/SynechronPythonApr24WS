nos = [1,2,3,4,2,3,8]
print(nos)
nos[0]= 100
print(nos)

nos.append(50)
print(nos)
names=[]
names.append('shalini')

colors1 = ['red','green']
color2 = ['blue','orange','black']
# print(colors1+color2)
# print(colors1)
# print(color2)

# print(colors1.append(color2))
# print(colors1)
# print(color2)

# print(colors1.extend(color2))
# print(colors1)
# print(color2)

# timeslots=[[1,2,3,4],[4,5,6,7]]
print(id(colors1))
print(id(color2))
# colors1 = colors1 + color2
# print(id(colors1))
# print(id(color2))

colors1 += color2
print(id(colors1))
print(id(color2))
#[100, 2, 3, 4, 2, 3, 8, 50]
nos.remove(2)
print(nos)
print(nos.pop(0))
print(nos)

# nos.reverse()

values=[1,2,4,9,1,4,3,6]
# values.sort() # does in place sorting
# print(values)

data = sorted(values, reverse=True)
print(data)
print(values)

n1=[1,2]
n2=[3,4]
# print(n1*n2)
print()
names=['Sh','sonal','Arpita','Bin','nareshajkh']
print(names[0])
print(names[-1])
print(sorted(names, key=len))

print(sorted(names, key=str.lower))

val = 20
list1 = [5, 20, 15, 20, 25, 50, 20]
res = []
for l in list1:
    if l not in res:
        res.append(l)
print(res)