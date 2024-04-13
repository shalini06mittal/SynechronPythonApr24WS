person = '{"fname":"shalini","languages":["english","hindi"],"address":[{"city":"C1","street":{"street1":"some street"}},{"city":"C2"}]}'

import json
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])

# with open('person.txt','w') as file:
#     json.dump(person_dict, file) # will actually write the content of dict to a file

with open('person.json','w') as file:
    json.dump(person_dict, file,indent=4)

with open('student.json') as file:
    data = json.load(file)

print(data)
print(json.dumps(person_dict)) # converts python dict to json
