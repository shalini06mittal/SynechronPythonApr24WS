i=1
while i<=5:
    print(i)
    i+=1

no = 0
while no is not None:
    no = int(input('enetr a value'))
    if no<0:
        print('Neg')
    elif no>0:
        print('pos')
    else:
        print('its zero')
    ans = input('want to exit yY')
    if ans == 'y' or ans == 'Y':
        no = None