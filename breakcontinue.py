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

An electric mountain railway makes a return trips every day. 
In a trip the train goes up the mountain and back down. 

The train leaves from the foot of the mountain at 09:00, 11:00, 13:00 and 15:00.
The train returns from the top of the mountain at 10:00, 12:00, 14:00 and 16:00. 

Train can accomodate 200 passengers.

Passengers can only purchase a return ticket; all tickets must be purchased on the day of travel. 
The cost is $25 for the journey up and $25 for the journey down. 

Passengers must book their return train journey, as well as the departure train journey, when they
purchase their ticket.

Passengers can return on the next train down the mountain or a later train.

Task: Purchasing tickets.
1. Ask for number of tickets to purchase and if available go ahead asking time slots to book.
2. Ask user to enter departure time until they enter the right time as the time slots available 
3. Ask user to enter return time until they enter the right time as the time slots available and it should be 
after the departure time.
4.  Calculate total and print for return journey for 1 passenger 



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


