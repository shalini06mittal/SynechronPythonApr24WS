# loop - do something again and again
# range => start, stop, step

# start = 0, stop ? and is exclusive, step = 1
# print(list(range(10))) # stop-1, 
# print(list(range(1,11)))
# print(list(range(2, 101, 2)))
# print(list(range(10,1,-1)))

'''
for(i=1;i<=10;i++)
for var in <range of values>
'''

# for i in range(10):
#     print(i, i*i)

# for value in "":
#     print('hey')

# fixed set of values
# taking input annual sales for past 5 years and you want o calculate avergae
# total = 0
# for year in range(2019, 2024):
#     # Enter sales for year 2019
#     sale = float(input('enter sales for year: '+str(year)+'\n'))
#     total+=sale

# print('Average',total/5)

# ASCII Values
for v in "Hey there 123":
    print(v, ord(v)) # ord - ascii of character passed

for i in range(65, 71):
    print(i, chr(i)) # chr - gives character for ascii code passed


print(ord('h'))
print(chr(10000))