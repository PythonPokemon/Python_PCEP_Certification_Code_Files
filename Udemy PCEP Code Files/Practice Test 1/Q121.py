"""
Frage 24
Übersprungen
Q121

What is the expected output of the following code?

def func(x):
    return 1 if x % 2 != 0 else 2
 
print(func(func(1)))
--------------------------------------------------
Richtige Antwort
1
"""

def func(x):
    return 1 if x % 2 != 0 else 2   # wenn das argument x geteilt durch 2 Modulo rest ungleich 0 ist == 1 | sonst 2 


print(func(func(1)))  # 1

print(1 % 2)          # 1
print(1 % 2 != 0)     # True

