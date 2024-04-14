import pandas as pd
import numpy as np
years = range(2020, 2024)
shop1 = pd.Series([1000,1200,1150,1500], index=years)
shop2 = pd.Series([900,1100,1050,2500], index=years)
shop3 = pd.Series([1200,1500,1250,1900], index=years)

shops_df = pd.concat([shop1, shop2, shop3], axis=1)
shops_df.columns = ['shop1','shop2','shop3']
print(shops_df)
# print(shops_df['shop1'])
print()
# print(shops_df[0:2])

print(shops_df.apply(np.sum))
print(shops_df.apply(np.sum, axis=1))

d1 ={'Name':['Alisa','Bobby','Cathrine','Aliya','Bob','Katrina',],
    'Exam':['Semester 1','Semester 1','Semester 2','Semester 1','Semester 2','Semester 1'], 
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science'],
    'Score':[62,47,55,74,31,77]}
d2 = {'Name': ['Rahul', 'Naysa', 'Susy', 'Sheela', 'Shyam', 'Ram', ],
      'Exam':['Semester 3', 'Semester 3', 'Semester 2', 'Semester 1', 'Semester 2', 'Semester 1'],     
      'Subject': ['French', 'Mathematics', 'English', 'Science', 'SST', 'Science'],
      'Score': [90, 78, 66, 74, 31, 77]  }

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
print(df1[df1['Exam']=='Semester 1'])
print()
print(df1[ (df1['Exam']=='Semester 1') & (df1['Score'] >70) ])
print(df1.columns)
print(df1.values)
