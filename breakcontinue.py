# break and continue

# math
import math
# print('Enter 10 numbers or -1 to exit')

# breaj conditionally
# for i in range(1,11):
#     no = int(input('enter no '+str(i)))   
#     if no == -1:
#         print('Thanks!!')
#         break
#     print(no, math.pow(no,3))

# for i in range(1,60):
#     if i%3==0:
#         continue
#     print(i**3)

'''
find if a number entered is prime number or not. 


ask the user to enter a 2-digit 

Assume there are limited tickets for a day say 20.
Keep taking input for different customers until no tickets are left
WAP for a booking system of the adventurous park. 
Take input as customer phone number, count of people and 
age of every count (<=5 - 70/-, >5 and <18 – 120/-, above 18 – 150/-) visiting.
Calculate the phone total amount that customer has to pay along with the phone number.

'''
#puneet
# number=int(input("Enter the number: "))

# flag=1
# for num in range(3,number//2):
#     if(number%num==0):
#         flag=0
#         break

# if flag==1:
#     print("Num is prime")
# else:
#     print("Num is not prime")

num = int(input("Enter the Value for valdiate prime nunber or not"))

'''
if a no is divisible by any number bet 2 to no-1 , it is not prime
7 - 2 to no/2

6 - 
15, 49
when can we confirm no is prime?
only after dividing by all the numbers from 2 to n-1
'''
flag = 0
# sathish
for i in range(2, (num//2)+1): # 10, flag = 1: 7
    if(num % i ) == 0:
        print("not Prime number" + str(num))
        flag = 1
        break
if flag == 0:
    print(num,'is prime')

# else block for-else or while-else


