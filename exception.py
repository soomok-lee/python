# ninth chapter
# exception handling

try:
    print("-- division calculator --")
    nums = []
    nums.append(int(input("input first number : ")))
    nums.append(int(input("input second number : ")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("error! wrong input!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("unknown error occured!")
    print(err)

try:
    print("-- a digit calculator --")
    num1 = int(input("input first number : "))
    num2 = int(input("input second number : "))
    if num1 >= 10 or num2 >= 10:
       raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("error! wrong input! please input a digit.")

# custom Error
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

try:
    print("-- a digit calculator --")
    num1 = int(input("input first number : "))
    num2 = int(input("input second number : "))
    if num1 >= 10 or num2 >= 10:
       raise BigNumberError("input : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("wrong input! please input a digit.")
except BigNumberError as err:
    print("error! please input a digit.")
    print(err)
# finally
finally:
    print("thanks for using the calculator.")

# quiz 9
chicken = 10
waiting = 1

class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg

while(True):
    try:
        print("[total chicken : {0}]".format(chicken))
        order = int(input("how many chickens do you want to order?"))
        if order <= 0:
            raise ValueError
        elif order > chicken:
            print("sorry, we're short of chicken.")
        else:
            print("[waiting no {0}] {1} chicken(s) ordered.".format(waiting, order))
            waiting += 1
            chicken -= order
        
        if chicken == 0:
            raise SoldOutError("sold out.")
    except ValueError:
        print("wrong input!")
    except SoldOutError as err:
        print(err)
        break

