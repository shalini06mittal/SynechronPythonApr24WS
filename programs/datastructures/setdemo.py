#Create a set
s1 = {1000,123,2,453787897,1000,5,8,9}
print(type(s1))
s2=set()
print(type(s2))
s1.add(10)
s1.add(20)
print(s1)
s2={2,3,5,67,45}
s1.update(s2)
print(s1)
print(s2)
n1 = {1,2,3,4,5}
n2 = {1,2,3,6,7}
print()
print(n1.union(n2))
print(n1)
print('intersction')
print(n1.intersection(n2))
print(n2.intersection(n1))
print('diff')
print(n1.difference(n2))
print(n2.difference(n1))

