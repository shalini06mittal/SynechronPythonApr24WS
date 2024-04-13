# print('program starts')
# try:
#     print(10/0)
# except:
#     print('somethig went wrong')
# print('program continus')
# print('ends')

# nums =[1,'2a',3,4,5]
# try:
#     print(int(nums[1])/0)
# except IndexError :
#     print('index error')
# except ZeroDivisionError:
#     print('zero division error')
# except Exception:
#     print('please contact admin')

import math
def calculate(no):
    if no <=0:
        raise Exception('no shoud be > 0')
    print('Sqrt root of',no,':',math.sqrt(no))

calculate(100)
try:
    calculate(10)
except Exception as e:
    print('error',e)
finally:# close the resources , all the clean up
    print('finally called')