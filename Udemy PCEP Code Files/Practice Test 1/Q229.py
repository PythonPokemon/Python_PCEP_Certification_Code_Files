"""
Frage 94
Übersprungen
Q229

What is the expected output of the following code?
x = 1 + 1 // 2 + 1 / 2 + 2
print(x)
--------------------------------------------------
Richtige Antwort
3.5
"""

#   1 +    0   +  0,5  + 2      == 3,5
x = 1 + 1 // 2 + 1 / 2 + 2
print(x)                         # 3.5

print(1 + 1 // 2 + 1 / 2 + 2)    # 3.5

print(1 + (1 // 2) + 1 / 2 + 2)  # 3.5
print(1 + 0 + 1 / 2 + 2)         # 3.5

print(1 + 0 + (1 / 2) + 2)       # 3.5
print(1 + 0 + 0.5 + 2)           # 3.5

print((1 + 0) + 0.5 + 2)         # 3.5
print(1 + 0.5 + 2)               # 3.5

print((1 + 0.5) + 2)             # 3.5
print(1.5 + 2)                   # 3.5

print(3.5)                       # 3.5
