# tenth chapter
# module
# extension : .py

# theater_module.py
# import theater_module
# theater_module.price(3) 
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(2)
# mv.price_morning(3)
# mv.price_soldier(4)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# # price_soldier(7)

# from theater_module import price_soldier as price
# price(5) # price_soldier

# package
# a group of modules
# folder travel
# import travel.thailand # import module/package
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() 

# from travel.thailand import ThailandPackage # from - import module/class 
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

'''
from travel import *
to use 'import *', __init__.py - __all__
'''
from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

import inspect
import random
print(inspect.getfile(random)) # C:\Python39\lib\random.py
print(inspect.getfile(thailand)) # C:\git\python\travel\thailand.py

# quiz 10
'''
my own signature module - byme.py
'''
import byme
byme.sign()
