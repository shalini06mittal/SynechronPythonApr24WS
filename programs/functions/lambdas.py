def call(msg):
    print('Message as follows:\n', msg)
    # return "data"

# call('please meet')
message = call
# print(message("jgkjgjkg"))

def squares(no):
    return no**2

lambda no: no**2

def loginUser(username, password):
    return username == 'shalini' and password == 'sh'

lambda username, password: username == 'shalini' and password == 'sh'

def calculate(data, f): # f = squares
    # print(f)
    print([f(d) for d in data])
    # for d in data:
    #     print(f(d))

n1 = [1,2,3,3,45,6,7,8,9]
calculate(n1, squares)
calculate(n1, lambda no: no**2)
calculate(n1, lambda no: no**3)
calculate(n1, lambda no: no**1/5)
calculate(n1, lambda x: x%2==0)
calculate(n1, lambda x: x if x%2==0 else 0)
# lambdas
'''
1. def -> keyword lambda
2. function name () NOT
3. input -> arguments
4. logic
5. return
1 liners
lambda (arguments) : BL [ may or may not return a value]
'''


greetmsg = lambda : print('good evening')
greetmsg()
add = lambda a,b: a+b
print(add(2,3))

res = lambda nos : [n+10 for n in nos]

print(res([1,2,3,4,5]))

'''
Write a lambda function that takes 2 arguments as numbers and return the product of 2 numbers
'''

