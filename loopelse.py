#else is a block that gets executed iff the for loop completes the entire execution
# and not forcefully exit using break

for i in range(1,6):
    if i%10==0:
        print('BYe')
        break
    print(i+5)
else:
    print('else executed')

num = int(input("Enter the Value for valdiate prime nunber or not"))
for i in range(2, (num//2)+1): # 10, flag = 1: 7
    if(num % i ) == 0:
        print("not Prime number" + str(num))
        break
else:
    print(num,'is prime')