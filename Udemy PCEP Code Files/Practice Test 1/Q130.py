"""
Frage 13
Übersprungen
Q130

What is the expected output of the following code?

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

Richtige Antwort
17.5
"""

#   0,5   +   1    + 16
x = 1 / 2 + 3 // 3 + 4 ** 2       # potenz 4**2 == 16
print(x)                          # 17.5

print(1 / 2 + 3 // 3 + 4 ** 2)    # 17.5

print(1 / 2 + 3 // 3 + (4 ** 2))  # 17.5
print(1 / 2 + 3 // 3 + 16)        # 17.5

print((1 / 2) + 3 // 3 + 16)      # 17.5
print(0.5 + 3 // 3 + 16)          # 17.5

print(0.5 + (3 // 3) + 16)        # 17.5
print(0.5 + 1 + 16)               # 17.5

print((0.5 + 1) + 16)             # 17.5
print(1.5 + 16)                   # 17.5

print(17.5)                       # 17.5
