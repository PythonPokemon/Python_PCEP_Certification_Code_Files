
# Reading a variable inside of a function:
value1 = 23


def my_function1():
    print(value1)


my_function1()  # 23

# Trying to write a variable inside of a function:
value2 = 42


def my_function2():
    value2 = 67


my_function2()
print(value2)  # 42

# global, the something more that is needed:
value3 = 74


def my_function3():
    global value3
    value3 = 99


my_function3()
print(value3)  # 99
