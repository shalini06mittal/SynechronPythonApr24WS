def validate(email):
    return email.endswith('synechron.com')

def maxofnos(n1, n2):
    if n1>n2:
        return n1
    return n2

country='INdia'
city='Mumbai'
print('hey')
# print(__name__)
if __name__ == '__main__':
    print('1',__name__) 
    print('3',maxofnos(5,10))