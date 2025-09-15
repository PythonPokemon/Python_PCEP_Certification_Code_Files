"""
Frage 202
Übersprungen
Q416
Consider the following code.

x = [0, 1, 2]
x[0], x[2] = x[2], x[0]

What does the second assignment do?

Richtige Antwort
It reverses the list.
"""

x = [0, 1, 2]
x[0], x[2] = x[2], x[0]

print(x)     # [2, 1, 0]

# An even simpler one line swap:
y, z = 3, 7
y, z = z, y
print(y, z)  # 7 3
