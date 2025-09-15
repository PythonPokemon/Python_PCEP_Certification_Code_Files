"""
Frage 109
Übersprungen
Q527

You want to write a programm that asks the user for a value.
For the rest of the programm you need a whole number,
even if the user enters a decimal value.
What would you have to write?
------------------------------------------------------------
Richtige Antwort
num = int(float(input('How many do you need?')))
"""


# num = int(float(input('How many do you need?')))   # Eingabe -> erst float, dann int

num = int(float('7.3'))      # String '7.3' -> float 7.3 -> int 7
print(num)                   # 7

print(float('7.3'))          # String '7.3' -> float 7.3
print(str('7.3'))            # String bleibt String '7.3'
# print(int('7.3'))          # ❌ ValueError, weil '7.3' kein gültiger Integer-String ist
