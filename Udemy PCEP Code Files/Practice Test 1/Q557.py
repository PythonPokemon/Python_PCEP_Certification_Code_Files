"""
Frage 99
Übersprungen
Q557

The print() function is an example of:
--------------------------------------
Richtige Antwort
a Python built-in function
"""


built_ins = dir(__builtins__)
c = 0
for i in built_ins:
    if i[0] != '_' and i[0].islower():
        c = c + 1
        print(i, end=' ')
        if c % 10 == 0:
            print()
            
# abs all any ascii bin bool breakpoint bytearray bytes callable
# chr classmethod compile complex copyright credits delattr dict dir divmod
# enumerate eval exec exit filter float format frozenset getattr globals
# hasattr hash help hex id input int isinstance issubclass iter
# len license list locals map max memoryview min next object
# oct open ord pow print property quit range repr reversed
# round set setattr slice sorted staticmethod str sum super tuple
# type vars zip
