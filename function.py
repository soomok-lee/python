# sixth chapter
# function

# bank
def open_account():
    print("New account is created.")

def deposit(balance, money):
    print("deposit completed. your balance : {0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("withdraw completed. your balance : {0}".format(balance - money))
        return balance - money
    else:
        print("withdraw not completed your balance : {0}".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

open_account()

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(balance)
commission, balance = withdraw_night(balance, 500)
print("commission : {0}, balance : {1}".format(commission, balance))

# default value
def profile1(name, age=17, main_lang="python"):
    print("name : {0}, age : {1}, main_lang : {2}".format(name, age, main_lang))
 
profile1("Ella")

# keyword value
def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name = "Ella", main_lang = "python", age = 20)

# variable argument
# def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\tage : {1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)
# profile3("Ella", 20, "python", "java", "C", "C++", "C#")

def profile3(name, age, *lang):
    print("name : {0}\tage : {1}\t".format(name, age), end = " ")
    for l in lang:
        print(l, end=" ")
    print()

profile3("Ella", 20, "python", "java")

# local variable & global variable
gun = 10
def checkpoint(soldiers):
    # gun = 20 # local variable
    
    global gun # to use global variable gun
    '''not recommended, hard to manage global variables'''

    gun = gun - soldiers
    print("gun cnt in checkpoint: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("gun cnt in checkpoint: {0}".format(gun))
    return gun

print("gun cnt : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2) 
print("gun cnt : {0}".format(gun))

# quiz 6
def std_weight(height, gender): # height unit : m
    if gender == "male":
        return height*height*22
    else:
        return height*height*21

height = 175 # unit cm
gender = "male"
weight = round(std_weight(height/100, gender), 2)
print("height {0}cm {1} - std_height : {2}kg".format(height, gender, weight))