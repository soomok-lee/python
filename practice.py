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
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + " 일로 선정되었습니다.")