# fourth chapter
# control statement

# if
# weather  ="rain"
weather = input("how's the weather today?")
if weather == "rainy" or weather == "snowy":
    print("an umbrella")
elif weather == "fine dust":
    print("a mask")
else:
    print("none")

temp = int(input("how's the temperature?"))
if 30 <= temp:
    print("too hot, stay home.")
elif 10 <= temp and temp < 30:
    print("nice weather!")
elif 0 <= temp and temp < 10:
    print("wear a coat.")
else:
    print("too cold, stay home.")

# for
# for waiting_no in [0, 1, 2, 3, 4]:
for waiting_no in range(5): # 0, 1, 2, 3, 4
    print("waiting no : {0}".format(waiting_no))

starbucks = ["ironman", "thor", "spiderman"]
for customer in starbucks:
    print("{0}, your coffee is ready.".format(customer))

# while
customer1 = "thor"
index = 5
while index >= 1:
    print("{0}, your coffee is ready. {1} time(s) left.".format(customer1, index))
    index -= 1
    if index == 0:
        print("your coffee has been disposed of.")

customer2 = "ironman"
index = 1
while True:
    print("{0}, your coffee is ready. It has been called {1} time(s).".format(customer2, index))
    index += 1

customer3 = "spiderman"
person = "unknown"

while person != customer3:
    print("{0}, your coffee is ready.".format(customer3))
    person = input("what's your name?")

# continue - break
absent = [2, 5]
no_book = [7]
for student in range(1, 11): # 1 ~ 10 
    if student in absent:
        continue
    elif student in no_book:
        print("{0}, you are doomed. Follow me.".format(student))
        break
    print("{0}, please read the book.".format(student))

# one line for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["ironman", "thor", "spiderman"]
students = [len(i) for i in students]
print(students)

students = ["ironman", "thor", "spiderman"]
students = [i.upper() for i in students]
print(students)

# quiz 5
from random import *
cnt = 0 # total customers
for i in range(1, 51):
    time = randrange(5,51)
    if 5 <= time <= 15:
        print("[O] customer {0} (time : {1} minutes)".format(i,time))
        cnt += 1
    else:
        print("[ ] {0} customer (time : {1} minutes)".format(i,time))
    
print("total customers : {0}".format(cnt))