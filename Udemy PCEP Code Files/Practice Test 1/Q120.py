"""
Frage 88
Übersprungen
Q120

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
1 1 2
"""


x = 1
y = 2

x, y, z = 1, 1, 2  # -> x=1; y=1; z=2
z, y, z = 1, 1, 2  

print(x, y, z)     # 1 1 2
