# matrix multiplcation and time calculation Using random number selection.
import random
import time
import datetime
a = []
b = []

# N of value of 32
def thirty2():
    for i in range(32):
        a.append([random.randint(0, 11) for x in range(1, 33)])
    for j in range(32):
        b.append([random.randint(0, 11) for x in range(1, 33)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

# N of value of 64
def sixty4():
    for i in range(64):
        a.append([random.randint(0, 11) for x in range(1, 65)])
    for j in range(64):
        b.append([random.randint(0, 11) for x in range(1, 65)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

# N of value of 128
def one28():
    for i in range(128):
        a.append([random.randint(0, 11) for x in range(1, 129)])
    for j in range(128):
        b.append([random.randint(0, 11) for x in range(1, 129)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()


# N of value 256
def two56():
    for i in range(256):
        a.append([random.randint(0, 11) for x in range(1, 129)])
    for j in range(256):
        b.append([random.randint(0, 11) for x in range(1, 129)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()


# N of value 512
def five12():
    for i in range(512):
        a.append([random.randint(0, 11) for x in range(1, 513)])
    for j in range(512):
        b.append([random.randint(0, 11) for x in range(1, 513)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

while True:
    print("Start of program time : ", datetime.datetime.now())
    print("-------------------------")
    print("Add N as 32, 64, 128, 256, or 512 ---- 0 to exit")
    x = int(input("Enter N: "))
    if x == 32:
        print("Before Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print(thirty2())
        print("-------------------------")
        print("After Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        print("End of program time : ", datetime.datetime.now())
        break
    if x == 64:
        print("Before Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print(sixty4())
        print("-------------------------")
        print("After Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        print("End of program time : ", datetime.datetime.now())
        break
    if x == 128:
        print("Before Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print(one28())
        print("-------------------------")
        print("After Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        print("End of program time : ", datetime.datetime.now())
        break
    if x == 256:
        print("Before Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print(two56())
        print("-------------------------")
        print("After Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        print("End of program time : ", datetime.datetime.now())
        break
    if x == 512:
        print("Before Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print(five12())
        print("-------------------------")
        print("After Execution, time : ",datetime.datetime.now())
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        print("End of program time : ", datetime.datetime.now())
        break
    if x == 0:
        print("-------------------------")
        print("Thank you for taking part")
        break