msg='Welcome Guest'
print(len(msg))
print(msg.count('e'))
print(msg.endswith('Guest'))
print(msg.upper())
print(msg.lower())

print('index',msg.index('e'))
print(msg.index('e', 2))
# username -   shalini  
#dbusername = shalini
desc = '     some     description     '
print('***'+desc+'***')
print('***'+desc.rstrip()+'***')
print('***'+desc.lstrip()+'***')
print('***'+desc.strip()+'***')

print('Hey {0} and heres you lucky number{1}'.format(msg, 5))
# slicing 
# http://
url ='http://www.techgatha.com'
# start:stop:step
print(url[0:7]) # http://
print(url[7:])# www.techgatha.com
print(url[:7])# http://
print(url[5:])# //www.techgatha.com
print(url[0:len(url):5])# h/.g.
print(msg[::-1])# tseuG emocleW

print('1',msg[len(msg)::-1])
# print(msg[len(msg)])

# separate the name and domain name

email='shalini@gmail.com'

index = email.index('@')
print(email[0:index])
print(email[index:])

# the format of file location does not change. 
#from the file location print the name and extension of image seaparate.
fileloc = 'file://C:/images/pic1.jpg'
# print(fileloc.rindex('@'))
index = fileloc.rfind('/')
if index!=-1:
    dotindex = fileloc.index('.')
    print('filename', fileloc[index+1: dotindex])
    print('extension', fileloc[dotindex+1:])
