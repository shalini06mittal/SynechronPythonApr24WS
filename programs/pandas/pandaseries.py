import pandas as pd
import numpy as np
# series -> 1-D

a=[10,12,30,4,54]
s1 = pd.Series(a, index=['oranges','apples','grapes','mangoes','bananas'])
s2 = pd.Series([5,9,12,59,60], index=['oranges','apples','grapes','mangoes','bananas'])
print(s1)
print(s1+s2)
# dataframes -> 2-D
print(s1['oranges'])
print(s1[['oranges','mangoes']])

salary = pd.Series([100,200,120,300],index=['e1','e2','e3','e4'])
print(salary)
print(salary + salary * 0.10)

print(salary.apply(np.log))
def deduct(sal):
    return sal - sal *0.5

print(salary.apply(deduct))