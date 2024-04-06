'''
datat types
int
float
bool - True and False
string
complex
None
'''
print(type(10))
print(type('10'))
print(type(10.34))
print(type(True))
print(type(10+3j))

# variables - used to store values
x = 10
print(x)
print(type(x))
x = 'hi'
print(type(x))
x = True
print(type(x))
y=10
x=20
# 10 + 20 = 30
# separator i.e space and default end that is \n
print(y,'+',x,'=',x+y, sep='!', end='\t')
print(y,'-',x,'=',y-x)

a,b,c=1,2,3

a=10
b=20
a,b=b,a