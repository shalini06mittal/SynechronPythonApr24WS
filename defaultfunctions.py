# default and positional argument
# default argument - 
def takeOrder(item, drink, desert='brownie'):
    print('Here is your order')
    print('Take your',item,'with your',drink,'and',desert)

takeOrder('pizza','coke','brownie')
# takeOrder('pizza','coke')
# keyword argument
print('1.')
takeOrder('burger',drink='milk')
print('2.')
takeOrder('sanwich','limca')
takeOrder(desert='cake',item='sanwich',drink='limca')
# * -> arbitrary argument
def myprint(*values, p=1):
    print(values)

myprint(1,2,3,4,5,p=2)
# arbitrary keyword arguments
def func(**kwargs):
    print(kwargs)
func(v=1,n=2,colors=['red','green'])