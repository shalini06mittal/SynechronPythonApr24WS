import numpy as np

x,y,z = np.loadtxt('values.txt', skiprows=1, unpack=True)
print(x,y,z)

values= np.loadtxt('values.txt', skiprows=1)
print(values)

# values= np.genfromtxt('valuesmiss.txt',skip_header=1, filling_values=-1)
# print(values)

arr = np.arange(1,11,2)
print(arr)
np.savetxt('test.txt', arr, delimiter=',')