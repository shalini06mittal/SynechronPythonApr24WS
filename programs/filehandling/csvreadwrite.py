import csv
# file = open('employees.csv',newline='', 'w')
# writer = csv.writer(file)
# writer.writerow(['Id','Name','Phone'])
# writer.writerow(['1','shalini','876879797'])
# writer.writerow(['2','sonal','0897987'])
# writer.writerow(['3','sunil','123213'])
# writer.writerow(['4','sathish','45654363'])
# writer.writerows([['5','naresh','265464'],['6','yogesh','3897987']])
# file.close()

# with open('employees.csv', '+a') as file:
#     writer = csv.writer(file)
#     writer.writerow(['7','nisha','5768768'])

# header
with open('employees.csv','r') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    print()
    for row in reader:
        print(row)
print('reading invoice')
with open('invoice.csv','r') as file:
    reader = csv.reader(file, delimiter=':')
    header = next(reader)
    print(header)
    print()
    for row in reader:
        print(row)

print('reading invoice with dict')
with open('invoice.csv','r') as file:
    reader = csv.DictReader(file, delimiter=':')
    header = next(reader)
    print(header)
    print()
    for row in reader:
        print(row)