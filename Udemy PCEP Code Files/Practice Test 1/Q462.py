"""
Frage 116
Übersprungen
Q462

What is the expected output of the following code?
---------------------------------------------------------------------
Richtige Antwort
1
---------------------------------------------------------------------
"""


v = 1


def fun():
    global v
    v = 2
    return v


print(v)  # 1
print(fun())  # 2