"""
Frage 26
Übersprungen
Q617

What is the expected output of the following code?

def func(x, y, z):
    return x + 4 * y + 5 * z
 
 
print(func(1, z=2, y=3))
---------------------------------------------------
Richtige Antwort
23
"""

def func(x, y, z):
    return x + 4 * y + 5 * z


print(func(1, z=2, y=3))      # 23 | 1 + 4*3+ 5*2 == 1 + 12 + 10 == 23

print(1 + 4 * 3 + 5 * 2)      # 23
print(1 + (4 * 3) + (5 * 2))  # 23
print(1 + 12 + 10)            # 23
print(23)                     # 23
