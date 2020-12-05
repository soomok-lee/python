# fourth chapter
# data structure

# List []

# subway
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["Ella", "Mari", "Jessie", "Lia"]
# index of Mari
print(subway.index("Mari"))
# append Runa
subway.append("Runa")
print(subway)

# insert Lydia between Ella and Mari
subway.insert(1, "Lydia")
print(subway)

# pop
print(subway.pop())
print(subway)

# count how many people have the same name
subway.append("Ella")
print(subway)
print(subway.count("Ella"))

# sort order
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# reverse order
num_list.reverse()
print(num_list)

# clear
num_list.clear()
print(num_list) # []

# mix variables
mix_list = ["Ella", 20, True]
print(mix_list)
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)

# Dictionary

cabinet = {3:"Ella", 100:"Mari"}
print(cabinet[3]) # Ella
print(cabinet[100]) # Mari

print(cabinet.get(3)) # Ella
# print(cabinet[5]) # error
print(cabinet.get(5)) # none

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"Ella", "B-100":"Mari"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

# new guest
cabinet["C-20"] = "Lydia"
# update
cabinet["A-3"] = "Jessie"
print(cabinet)

# delete
del cabinet["A-3"]
print(cabinet)

# print keys only
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# print values only
print(cabinet.values()) # dict_values(['Mari', 'Lydia'])

# print key-value
print(cabinet.items()) # dict_items([('B-100', 'Mari'), ('C-20', 'Lydia')])

# clear
cabinet.clear()
print(cabinet)

# Tuple 
'''
faster than List
no changes allowed
'''
menu = ("hamburger", "pizza")
print(menu[0])
print(menu[1])
# menu.add("chicken")

# name = "Ella"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

(name, age, hobby) = ("Ella", 20, "coding")
print(name, age, hobby)

# Set
'''
No order
No duplication
'''
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}
java = {"Ella", "Mari", "Jessie", "Lia"}
python = set(["Lydia", "Ella"])

# intersection
print(java & python) # {'Ella'}
print(java.intersection(python)) # {'Ella'}

# union
print(java | python)
print(java.union(python))

# difference
print(java - python)
print(java.difference(python))

# add to the set
python.add("Mari")
print(python)

# remove from the set
java.remove("Ella")

# Change of date structure
menu = {"coffee", "milk", "juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# quiz 4
'''
use shuffle, sample
from random import *
ids = [1,2,3,4,5] 
print(ids)
shuffle(ids)
print(ids)
print(sample(ids, 1)) 
'''
from random import *
users = range(1, 21) # 1~ under 21
# print(type(users))
users = list(users)
# print(type(users))
shuffle(users)
winners = sample(users, 4)
print(" -- winners --")
print("chicken: {0}".format(winners[0]))
print("coffee: {0}".format(winners[1:]))
print(" -- congrats --")
