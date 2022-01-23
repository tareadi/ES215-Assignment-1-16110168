# matrix multiplcation and time calculation Using random number selection.
import random
import time
a = []
b = []

# N of value of 32
def thirty2():
    for i in range(32):
        a.append([random.uniform(1, 10) for x in range(1,33)])
    for j in range(32):
        b.append([random.uniform(1, 10) for x in range(1, 33)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

# N of value of 64
def sixty4():
    for i in range(64):
        a.append([random.uniform(1, 10) for x in range(1, 65)])
    for j in range(64):
        b.append([random.uniform(1, 10) for x in range(1, 65)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

# N of value of 128
def one28():
    for i in range(128):
        a.append([random.uniform(1, 10) for x in range(1, 129)])
    for j in range(128):
        b.append([random.uniform(1, 10) for x in range(1, 129)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()


# N of value 256
def two56():
    for i in range(256):
        a.append([random.uniform(1, 10) for x in range(1, 257)])
    for j in range(256):
        b.append([random.uniform(1, 10) for x in range(1, 257)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()


# N of value 512
def five12():
    for i in range(512):
        a.append([random.uniform(1, 10) for x in range(1, 513)])
    for j in range(512):
        b.append([random.uniform(1, 10) for x in range(1, 513)])
    soln = [[sum(x*y for x,y in zip(x_row,y_col)) for y_col in zip(*b)] for x_row in a]
    return soln
    a.clear()
    b.clear()

while True:
    print("-------------------------")
    print("Add N as 32, 64, 128, 256, or 512 ---- 0 to exit")
    x = int(input("Enter N: "))
    if x == 32:
        starttime = time.process_time()
        print(thirty2())
        print("")
        cpu_time = time.process_time() - starttime
        print ("System and CPU time : {:0.5f}s".format(cpu_time))
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        break
    if x == 64:
        starttime = time.process_time()
        print(sixty4())
        print("")
        cpu_time = time.process_time() - starttime
        print ("System and CPU time : {:0.5f}s".format(cpu_time))
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        break
    if x == 128:
        starttime = time.process_time()
        print(one28())
        print("")
        cpu_time = time.process_time() - starttime
        print ("System and CPU time : {:0.5f}s".format(cpu_time))
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        break
    if x == 256:
        starttime = time.process_time()
        print(two56())
        print("")
        cpu_time = time.process_time() - starttime
        print ("System and CPU time : {:0.5f}s".format(cpu_time))
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        break
    if x == 512:
        starttime = time.process_time()
        print(five12())
        print("")
        cpu_time = time.process_time() - starttime
        print ("System and CPU time : {:0.5f}s".format(cpu_time))
        print("-------------------------")
        print("Thank you for taking part please rerun for another set")
        break
    if x == 0:
        print("-------------------------")
        print("Thank you for taking part")
        break