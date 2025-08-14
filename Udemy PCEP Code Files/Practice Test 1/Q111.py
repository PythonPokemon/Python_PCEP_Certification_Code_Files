"""
da in der finktions deklaration  parameter definiert sind, die in der funktion verwendet werden
muss unten im funktionsaufruf auch jeweils soviele argumente übergeben werden
die dann in der funktion verwendet werden wurden.
"""

# funktion, mit 2 Parametern | (text, num)
def func(text, num):
    while num > 0:
        print(text)
        num = num - 1

# deshalb muss der funktionsaufruf auch 2 Parameter/argumente übergeben
# damit due funktion auch funktioniert
func('Hello', 3)
"""
Hello
Hello
Hello
"""
