l1=[1,2,3,4,5,6,7,8,9,10]
# map will iterate and process every value from the iterbale seq and return a map object with new values

def s1(no): return no**2

print(list(map(s1, l1)))

print(list(map(lambda v: v**3,l1)))

print([no**2 for no in l1])

print(list(filter(lambda x: x%2==0, l1)))

'''
Write a Python program to add two given lists using map and lambda.
nums1 = [1, 2, 3] nums2 = [4, 5, 6]
Output : [5,7,9]
'''
nums1 = [1, 2, 3] 
nums2 = [4, 5, 6]

print(list(map(lambda x,y:x+y, nums1, nums2)))
print([ x+y for x,y in zip(nums1,nums2) ])


l1=[1,2,3,4,5,6,7,8,9,10]
s=0
for n in l1:
    s+=n

print(s)

s=l1[0]
for i in range(1,len(l1)):
    s+=l1[i]

print(s)

from functools import reduce
print(reduce(lambda s, x: s+x, l1, 0))