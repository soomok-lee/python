# eighth chapter 
# class

# sample
# marine : unit, soldier
marine_name = "marine"
marine_hp = 40
marine_damage = 5

print("unit {0} is created.".format(marine_name))
print("hp {0}, damage {1}\n".format(marine_hp, marine_damage))

# tank : unit, tank
tank_name = "tank"
tank_hp = 150
tank_damage = 35

print("unit {0} is created.".format(tank_name))
print("hp {0}, damage {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : attack enemies in the {1} direction.".format(name, location, damage))

attack(marine_name, "one o'clock", marine_damage)
attack(tank_name, "one o'clock", tank_damage)

# class
class Unit:
     def __init__(self, name, hp, damage): # __init__ : constructor
         self.name = name # member variable
         self.hp = hp # member variable
         self.damage = damage # member variable
         print("unit {0} is created.".format(self.name))
         print("hp {0}, damage {1}\n".format(self.hp, self.damage))

marine1 = Unit("marine", 40, 5) # marine1 : instance of Unit class 
marine2 = Unit("marine", 40, 5)
tank = Unit("tank", 150, 35)

# member variable 
'''variables defined within a class'''

# wraith : unit, plane
wraith1 = Unit("wraith", 80, 5)
print("unit name : {0}, damage {1}".format(wraith1.name, wraith1.damage))

# mind control
wraith2 = Unit("wraith", 80, 5)
wraith2.clocking = True # assigned new variable 'clocking' outside the class 
if wraith2.clocking == True:
    print("{0} is on clocking.".format(wraith2.name))

# method
class AttackUnit:
     def __init__(self, name, hp, damage): # __init__ : constructor
         self.name = name # member variable
         self.hp = hp # member variable
         self.damage = damage # member variable

     def attack(self, location):
         print("{0} : attack enemies in the {1} direction. [damage {2}]"\
             .format(self.name, location, self.damage))

     def damaged(self, damage):
         print("{0} : damaged {1}".format(self.name, damage))
         self.hp -= damage
         print("{0} : hp {1}".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : destroyed.".format(self.name))

# firebat : AttackUnit, fire
firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("5 o'clock")

firebat1.damaged(25)
firebat1.damaged(25)