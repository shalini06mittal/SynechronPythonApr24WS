# import app
# print(app.validate('shalini@synechron.com'))
# print(app.maxofnos(23,45))

# create an alias
# import app as module

# print(module.maxofnos(3,6))
print('2',__name__)
from app import validate as val, maxofnos as mn, country
# print(val('shalini@gmail.com'))
# print(mn(2,5))
# print(country)
# print(dir())

# import app

import sys
sys.path.append('./programs/basic/')
import inputdemo
import operators