"""
immer wenn eine true or false möglichkeit besteht, ist es true!
Immer wenn eine false and true möglichkeit besteht, ist es false!
"""
z = 7
y = 3
x = y < z or z > y and y > z or z < y
print(x)                                  # True
print(y < z or z > y and y > z or z < y)  # True
print(3 < 7 or 7 > 3 and 3 > 7 or 7 < 3)  # True
print(True or True and False or False)    # True
print(True or (True and False) or False)  # True
print(True or False or False)             # True
print((True or False) or False)           # True
print(True or False)                      # True
print(True)                               # True
