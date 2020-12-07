# eighth chapter 
# inheritance
 
class Unit:
     def __init__(self, name, hp, speed): # __init__ : constructor
         self.name = name # member variable
         self.hp = hp # member variable
         self.speed = speed
    
     def move(self, location):
         print("[ground unit name]")
         print("{0} : move to the {1} direction. [speed {2}]"\
             .format(self.name, location, self.speed))

class AttackUnit(Unit):
     def __init__(self, name, hp, speed, damage): # __init__ : constructor
         Unit.__init__(self, name, hp, speed)
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

# multiple inheritance
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
         print("[flying unit name]")
         self.fly(self.name, location)


# firebat : attack unit, fire
# firebat1 = AttackUnit("firebat", 50, 5, 16)
# firebat1.attack("5 o'clock")

# firebat1.damaged(25)
# firebat1.damaged(25)    

# valkyrie : flying unit
# valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3 o'clock")

# vulture : ground unit
vulture = AttackUnit("vulture", 80, 10, 20)

# battlecruiser : flying unit
battlecruiser = FlyableAttackUnit("battlecruise", 500, 25, 3)

vulture.move("11 o'clock")
battlecruiser.move("9 o'clock")

# pass
# building
# class BuildingUnit(Unit):
#      def __init__(self, name, hp, location):
#         pass

# supply depot : building, a building = 8 unit
# supply_depot = BuildingUnit("supply depot", 500, "7 o'clock")

# def game_start():
#     print("game start")

# def game_over():
#     pass

# game_start()
# game_over()

# super
# building
class BuildingUnit(Unit):
     def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super - self X
        self.location = location

# multiple inheritance - super
class U:
    def __init__(self):
        print("U constructor")

class F:
    def __init__(self):
        print("F constructor")

class FU(U, F):
    def __init__(self):
        # super().__init__() # U constuctor
        U.__init__(self)
        F.__init__(self)

# dropship : flying unit
dropship = FU()
