import numpy as np

# scientific and mathematical
# array - homogeneous
l1 = [1,2,3,4,5]
print(l1)
arr = np.array(l1)
arr1 = np.array(l1, dtype=np.float32)
print(arr.dtype)
print(arr1.dtype)
print(arr+10)
print(arr)
arr[0]=100
print(arr)

tempinfah = np.array([98,97,93.34,100.2])
print((tempinfah -32) * 5/9)

ones = np.ones((5,3,1), dtype=np.int32)
print(ones)
zeroes = np.zeros((2,3))
print(zeroes)

print(ones.shape)
print(ones.size)
print(ones.itemsize)
print(ones.ndim)

rmarr = np.random.random((2,2))
print(rmarr)

rgarr = np.arange(1,100,5)
print(rgarr)
print(rgarr.reshape((2,10)))

idarr = np.identity(3)
print(idarr)
emarr = np.empty((3,2))
print(emarr)
fullarr = np.full((2,2),10)
print(fullarr)
spacearr = np.linspace(1,100,5, retstep=True)
print(spacearr)