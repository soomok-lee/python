# eighth chapter 
# inheritance

class Unit:
     def __init__(self, name, hp): # __init__ : constructor
         self.name = name # member variable
         self.hp = hp # member variable

class AttackUnit(Unit):
     def __init__(self, name, hp, damage): # __init__ : constructor
         Unit.__init__(self, name, hp)
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