# f1 = open('demo.txt', '+a')
# f1.write('hey there\n')
# f1.writelines(['apples\n','oranges\n'])
# f1.close()

f2 = open('demo.txt')
# data = f2.read()
# print(type(data))
# data = f2.readline()
# while data:
#     # print(type(data))
#     print(data.strip())
#     data = f2.readline()
# print(data)
data = f2.readlines()
print(type(data))
f2.close()
print(data)
print([line.strip().upper() for line in data])
'''
create a file email.txt to store list of 5 emails taken as input from the user
Create another file gmail.txt to store all the emails that end with gmail.com
'''

