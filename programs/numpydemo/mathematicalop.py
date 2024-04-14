import numpy as np

A = np.array([ [1,2,3], 
              [4,5,6], 
              [7,8,9] ]) 
B = np.ones((3,3)) 

# print(A*B)
# print(A.dot(B))
# print(A.T)
# print()
# print(A+B)
# print(np.add(A,B))
# print(np.subtract(A,B))
print(A)
print(np.sum(A))
print(np.min(A))
print(np.sum(A,axis=1))# runs thr columns
print(np.sum(A,axis=0))# runs through rows
print(np.min(A, axis=1))
print(np.min(A, axis=0))

newarr = np.append(A,[10,20,30])
print(newarr)
print(np.insert(newarr,1, 100))
print(newarr)
print(np.delete(newarr,[1,3]))

