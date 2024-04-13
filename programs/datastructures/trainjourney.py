'''

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
'''

Ask = int(input("How many tickets you want"))#201
while Ask > 200:
        Ask = int(input("Error, Please enter below 200"))


time_up = int(input("What time would you like to buy for 9 11 13 15?: "))
while time_up != 9 and time_up != 11 and time_up != 13 and time_up != 15 :
        print("Error! please select the appropraite time from the available.")
        time_up = int(input("What time would you like buy for 9 11 13 15?: "))
            
time_down = int(input("What time would you like to return 10 12 14 16?: "))
while time_up > time_down or ( time_down != 10 and time_down != 12 and time_down != 14 and time_down  != 16) :
        print("Error! please select the appropraite time (you must not select the time below the departure)." )
        time_down = int(input("What time would you like to return 10 12 14 16?: "))

cost = Ask * 2 * 25
print('totol',cost)


