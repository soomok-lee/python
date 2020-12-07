# starcraft

from random import *

class Unit:
     def __init__(self, name, hp, speed): # __init__ : constructor
         self.name = name # member variable
         self.hp = hp # member variable
         self.speed = speed
         print("{0} unit is created.".format(name))
    
     def move(self, location):
        #  print("[ground unit name]")
         print("{0} : move to the {1} direction. [speed {2}]"\
             .format(self.name, location, self.speed))

     def damaged(self, damage):
         print("{0} : damaged {1}".format(self.name, damage))
         self.hp -= damage
         print("{0} : hp {1}".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : destroyed.".format(self.name))


class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage): # __init__ : constructor
         Unit.__init__(self, name, hp, speed)
         self.damage = damage # member variable

     def attack(self, location):
         print("{0} : attack enemies in the {1} direction. [damage {2}]"\
             .format(self.name, location, self.damage))
    
# Marine
class Marine(AttackUnit):
     def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

     def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : used stimpack. (hp -10)".format(self.name))
        else:
            print("{0} : hp not enough.".format(self.name))

# Tank
class Tank(AttackUnit):
    # seize mode
     seize_developed = False

     def __init__(self):
         AttackUnit.__init__(self, "Tank", 150, 1, 35)
         self.seize_mode = False

     def set_seize_mode(self):
         if Tank.seize_developed == False:
             return
        
         if self.seize_mode == False:
             print("{0} : turn on seize mode.".format(self.name))
             self.damage *=2
             self.seize_mode = True
         else:
             print("{0} : turn off seize mode.".format(self.name))
             self.damage /=2
             self.seize_mode = False
         
class Flyable:
     def __init__(self, flying_speed):
         self.flying_speed = flying_speed

     def fly(self, name, location):
         print("{0} : fly to the {1} direction. [speed {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
     def __init__(self, name, hp, damage, flying_speed):
         AttackUnit.__init__(self, name, hp, 0, damage) # ground_speed = 0
         Flyable.__init__(self, flying_speed)

    # method overriding
     def move(self, location):
        #  print("[flying unit name]")
         self.fly(self.name, location)

# Wraith
class Wraith(FlyableAttackUnit):
     def __init__(self):
        FlyableAttackUnit.__init__(self, "wraith", 80, 20, 5)
        self.clocked = False

     def clocking(self):
         if self.clocked == True:
            print("{0} : tune off clocking mode.".format(self.name))
            self.clocked = False
         else:
            print("{0} : tune on clocking mode.".format(self.name))
            self.clocked = True
        
def game_start():
    print(" -- game start -- ")

def game_over():
    print(" -- game over -- ")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# all units move
for unit in attack_units:
    unit.move("1 o'clock")

# develop Tank's seize mode
Tank.seize_developed = True
print("[note] Tank's seize mode is developed.")

for unit in attack_units:
     if isinstance(unit, Marine):
        unit.stimpack()
     elif isinstance(unit, Tank):
        unit.set_seize_mode()
     elif isinstance(unit, Wraith):
         unit.clocking()

# all units attack
for unit in attack_units:
    unit.attack("1 o'clock")

# all units damaged
for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()

'''
Unit <- AttackUnit <- Marine, Tank 
Flyable <- FlyableAttackUnit
Unit <- AttackUnit <- FlyableAttackUnit - Wraith 
'''