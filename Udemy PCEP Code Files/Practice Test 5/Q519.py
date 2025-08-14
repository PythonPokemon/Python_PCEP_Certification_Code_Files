
x = 42
print(id(x))  # E.g. 4404291864


def func():
    global x
    print(id(x))  # E.g. 4404291864 (same number)
    print('1. x:', x)
    x = 23
    print('2. x:', x)


func()
print('3. x:', x)

"""
1. x: 42
2. x: 23
3. x: 23
"""
