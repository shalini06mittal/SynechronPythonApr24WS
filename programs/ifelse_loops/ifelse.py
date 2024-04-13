#condtitional constructs
'''
if <expression>:
    stat 1
    stat 2
else:
    stat 1
    stat 2
'''
# age = int(input('enter age'))
# if age >= 18:
#     print('can vote')
#     print('Please enter other details:- ')
# else:
#      print('cannot vote')


# a = (input("enter the frist value")) #
# b = (input("enter the frist value"))
# c = (input("enter the frist value"))
# d = (input("enter the frist value"))
# e = (input("enter the frist value"))
# f = a + b + c + d + e # 1 2 3 4 5
# print(int(f))

'''
1. cash
2. cc
3. neft
'''
# mode = int(input('Mode of payment\n1. Cash\n2. CC\n3. NEFT'))
# if mode == 1:
#     print('please pay cash at the tiem of delivery')
# elif mode == 2:
#     type = input('Choose 1. Master\n2. Visa')
#     if type==1:
#         print('enter details for master card')
#     else:
#         print('enter details for visa card')
# elif mode == 3:
#     print('Details of bank')
# else:
#     print('please enter values 1, 2 or 3 only')

# x = 10
# if x:
#     print('yes')
# else:
#     print('no')

# city = None
# if city:
#     print('city yes')
# else:
#     print('city no')



leapYear=int(input("Enter the year"))
# if leapYear%4==0:
#     if leapYear%100==0:
#         if leapYear % 400==0:
#             print("it is leap year")
#         else:
#             print("it is not a leap year")
#     else:
#         print("it is a leap year")
# else:
#     print("it is not a leap year")

if ( leapYear %4==0 and (leapYear %100 !=0 or (leapYear %100==0 and leapYear %400 ==0))):
    print('leap year')
else:
    print('not leap year')

