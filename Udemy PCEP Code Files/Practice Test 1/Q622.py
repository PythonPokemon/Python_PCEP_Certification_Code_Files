"""
Frage 66
Übersprungen
Q622

Consider the following code.

def function(x=0):
    return x

With sentence describes the function the best?

A function defined like ...function()
-----------------------------------------------------
Richtige Antwort
may be called without any argument, or with just one.
"""


def function(x=0):
    return x


print(function())        # 0
print(function(7))       # 7
# print(function(4, 7))  # TypeError: ...
