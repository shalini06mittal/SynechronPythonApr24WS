'''
Full stack dev 
java full - java, spring boot(REST API), hibernate, junit, microservices
python - python, django[WEB, REST, complex]/fastapi[RESt]/flask[WEB, REST]
ORM - sqlalchemy
database - sql , nosql
front - angular, reaact ,vue

devops - git linux docker kub jenkins AWS
maven

data analytics:
python, REST API(fastapi), numpy scipy pandas matplotlib 
'''
# concise way of writing the for loop
# newlist = [expression for member in list]

n1 = [1,2,3,3,45,6,7,8,9]
squares=[]
for n in n1:
    squares.append(n*n)
print(squares)

squares = [n*n for n in n1]
print(squares)

data='hey there and calculate vowels'
vowels ='aeiou'
vowelsindata = []
for d in data:
    if d in vowels:
        vowelsindata.append(d)
print(vowelsindata)

vowelsindata = [d for d in data if d in vowels]
print(vowelsindata)

prices = [20, 30, 40, 50, 60]
#new list with 10% discount added on evey price in prices
discountedprices = [0.9 * price for price in prices]
print(discountedprices)

#Combine the elements of two lists if they are not equal:

#Ex: list1= [1,2,3] list2=[3,1,4] 
# Output:
#[(1, 3),(0,0) (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
list1= [1,2,3] 
list2=[3,1,4] 
newlist = [(l1,l2) for l1 in list1 for l2 in list2 if l1!=l2]
print(newlist)

newlist = [(l1,l2) if l1!=l2 else (0,0) for l1 in list1 for l2 in list2 ]
print(newlist)



