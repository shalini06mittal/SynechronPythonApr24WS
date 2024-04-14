from datetime import datetime
import numpy as np
def numpysum(n): 
	a = np.arange(n) ** 2 
	b = np.arange(n) ** 3 
	c=a + b
	return c 

def pythonsum(n): 	
    a = list(range(n) )
    b = list(range(n)) 
    c = [] 
    for i in range(len(a)): 
        a[i] = i ** 2 
        b[i] = i ** 3 
        c.append(a[i] + b[i]) 
    return c


size = 10000000
start = datetime.now() 
c = pythonsum(size) 
delta = datetime.now() - start 
print("The last 2 elements of the sum", c[-2:]) 
print(c[9999999])
print("PythonSum elapsed time in microseconds", delta.microseconds )
start = datetime.now() 
c = numpysum(size) 
delta = datetime.now() - start 
print ("The last 2 elements of the sum", c[-2:])
print(c[9999999]) 
print("NumPySum elapsed time in microseconds", delta.microseconds )

