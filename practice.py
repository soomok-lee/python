# first chapter

# data type
# number
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
# string
print('apple')
print("banana")
print("lol")
print("lol"*9)
# boolean
print(5>10)
print(5<10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5>10))
# variable
animal = "puppy"
name = "Ella"
age = 4
hobby = "walking"
is_adult = age >= 3
print("my " + animal + "'s name is " + name)
print(name + " is " + str(age) + " years old")
print(name,"is",age,"years old")
hobby = "running"
print(name + "'s hobby is " + hobby)
print("is " + name + " an adult? " + str(is_adult))

# comment
# ctrl + '/'
'''comments'''

# quiz 1
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

# second chapter

# operator
print(1+1) # 2
print(4-2) # 2
print(2*5) # 10
print(6/3) # 2.0
print(7/2) # 3.5

print(2**3) # 2^3 = 8
print(5%3) # 2
print(10%3) # 1
print(5//3) # 1
print(10//3) # 3

print(10>3) # True
print(4>=7) # False
print(10<3) # Flase
print(5<=5) # True

print(3==3) # True
print(4==2) # False
print(3+4==7) # True    

print(1!=3) # True
print(not(1!=3)) # False
print((3>0) and (3<5)) # True  
print((3>0) & (3<5)) # True

print((3>0) or (3>5)) # True
print((3>0) | (3>5)) # True
print(5>4>3) # True
print(5>4>7) # False

# equation
print(2+3*4) # 14
print((2+3)*4) # 20
number = 2+3*4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2 # 18
print(number)
number *= 2 # 36
print(number)
number /= 2 # 18.0
print(number) 
number -= 2 # 16.0
print(number) 
number %= 5 # 1.0
print(number)

# number processing function
# absolute
print(abs(-5)) # 5
# power
print(pow(4, 2)) # 4^2 = 16
# max
print(max(5, 12)) # 12
# min
print(min(5, 12)) # 5
# round
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
# floor
print(floor(4.99)) # 4
# ceil
print(ceil(3.14)) # 4
# square root
print(sqrt(16)) # 4.0

# random function
from random import *
print(random()) # random number 0.0 ~ under 1.0 
print(random()*10) # random number 0.0 ~ under 10.0 
print(int(random()*10)) # random number 0 ~ under 10  
print(int(random()*10) + 1) # random number 0 ~ 10

print(randrange(1, 46)) # 1 ~ under 46
print(randint(1, 45)) # 1 ~ 45

# quiz 2
'''
condition
1. random number
2. between 4 and 28
3. print '오프라인 스터디 모임 날짜는 매월 #일로 선정되었습니다.'
'''
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")

# third chapter

# string
sentence = "I'm a girl"
print(sentence)
sentence2 = "Python is easy"
print(sentence2)
sentence3 = """
I'm a girl, and
Python in easy
"""
print(sentence3)

# slicing
jumin = "990120-1234567"
print("gender : " + jumin[7])
print("year : " + jumin[0:2])
print("month : " + jumin[2:4])
print("day : " + jumin[4:6])
print("birth date : " + jumin[:6]) # start from 0
print("last 7 digits : " + jumin[7:]) # to the last idx
print("last 7 digits : " + jumin[-7:]) # start from the last idx

# string processing function
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1)
print(index) # 15

print(python.find("Java")) # -1
# print(python.index("Java")) # error

print(python.count("n")) # 2 

# string format
print("a" + "b")
print("a","b")

# 1
print("I'm %d years old." % 20)
print("I like %s" % "python.")
print("Apple starts with %c." % "A")

# %s
print("I'm %s years old." % 20)
print("I like %s and %s colors." % ("blue","red"))

# 2
print("I'm {} years old.".format(20))
print("I like {} and {} colors.".format("blue", "red"))
print("I like {0} and {1} colors.".format("blue", "red"))
print("I like {1} and {0} colors.".format("blue", "red"))

# 3
print("I'm {age} years old and I like {color} color.".format(age = 20, color = "red"))
print("I'm {age} years old and I like {color} color.".format(color = "red", age = 20))

# 4 (v3.6~)
age = 20 
color = "red"
print(f"I'm {age} years old and I like {color} color.") 

# escape character
# \n 
print("How are you?\nGood.")
# \" \'
print("I'm 'ELLA'.")
print("I\'m \"ELLA\".")
print("I\'m \'ELLA\'.")
# \\
print("C:\\Users\\ella")
# \r 
print("Red Apple\rPine") # PineApple
# \b : backspace
print("Redd\bApple") # RedApple
# \t : tab
print("Red\tApple") # Red   Apple

# quiz 3
url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}, new password : {1}".format(url, password))

 