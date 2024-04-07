'''
Write a program to take 5 numbers and print factors of 5 numbers.
Ex: Input
10
Factors of 10 - 1 2 5 10
12
Factors of 12 - 1 2 3 4 6 12
.. So on for 5 numbers
'''

for i in range(5):
    no = int(input('enter a no'))
    print('factors of',no,'-',end=' ')
    for j in range(1,no+1):
        if no%j==0:
            print(j, end=' ')
    print()
'''
Assume for that day park admits only 50 customers. 
Modify the below code to provide for booking until the tickets are exhausted.
WAP for a booking system of the adventurous park. Take input as customer phone number, 
count of people and  age of every count(<=5 - 70/-, >5 and <18 – 120/-, above 18 – 150/-) visiting. 
Calculate the phone total amount that customer has to pay along with the phone number.
'''
availableTickets=50
ans='y'
customerCount = 0
while availableTickets>0:
    phone = input('enter phone number')
    count = int(input('enter number of tickets'))
    while count > availableTickets and ans=='y':
       print('Sorry!! available tickets are',availableTickets) 
       print('Please enter count less than or equal to',availableTickets)
       ans = input('Do you want to continue?y')
       if ans=='y':
            count = int(input('enter number of tickets'))
       else:
           ans ='n'
    customerCount+=1
    total = 0
    for c in range(1, count+1):
        age= int(input('enter age for customer '+str(c)))
        if age <= 5:
            total+=70
        elif age < 18:
            total+=120
        else:
            total+=150
    print('Booking details for customer',customerCount)
    print('Phone NUmber',phone)
    print('Total amount to pay', total)