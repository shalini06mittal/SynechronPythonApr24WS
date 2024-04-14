from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,11)
y = np.array([7,3,9,11,15,18,12,20,30,5])
print(x)
print(y)

plt.title('First Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
# plt.plot(x,y,'og')


# y = np.sin(x)
# plt.plot(x,y)
plt.bar(x,y,color='r', align='center')

plt.show()