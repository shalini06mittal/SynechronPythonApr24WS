person = '{"fname":"shalini","languages":["english","hindi"]}'

import json
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])

# with open('person.txt','w') as file:
#     json.dump(person_dict, file)

with open('person.json','w') as file:
    json.dump(person_dict, file,indent=2)

with open('student.json') as file:
    data = json.load(file)

print(data)
print(json.dumps(person_dict))
