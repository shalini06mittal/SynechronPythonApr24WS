# d1={}
# print(type(d1))
# d1['name'] = 'Shalini'
# d1['city'] = 'Pune'
# print(d1)

# employee={'name':'Satish','city':'Delhi' }
# print(employee)
# employee['name'] = 'Nisha'
# print(employee)
# employee['country'] = 'India'
# print(employee)
# print()
# print(employee.values())
# print(employee.keys())
# print(employee.items())
# key = 'name'
# print(employee.get(key))
# print(employee[key])
# key = 'phone'
# print(employee.get(key))
# # print(employee[key])

# for key in employee.keys():
#     print(key.upper(), end='\t')
# print()
# for value in employee.values():
#     print(value,end='\t')
# print()

# for key, value in employee.items():
#     print(key, ':', value)

players = ('P1','P2',"p3",'P4')
leaderboard = dict.fromkeys(players,0)
print(leaderboard)

for i in range(2):#20 30
    score = int(input('score for player 1'))
    leaderboard['P1']+=score
print(leaderboard)

employees = [
    {'name':'Satish','city':'Delhi' },
    {'name':'Sonal','city':'Pune' },
    {'name':'Amit','city':'Chennai' }
]
c=1
for employee in employees:
    print('Details of employee',c)
    for k,v in employee.items():
        print(k,':',v)
    print('------------------------------------------\n')
    c+=1
