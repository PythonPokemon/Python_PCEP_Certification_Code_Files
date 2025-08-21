"""
Beide Variablen enthalten denselben Text "Peter"
Python speichert nur eine Kopie im Speicher für unveränderliche Objekte wie Strings
Deshalb zeigen x und y auf dasselbe Objekt
-----------------------------------------------------------------------------------
is prüft, ob beide Variablen dasselbe Objekt im Speicher referenzieren
Da Python Speicher spart und "Peter" intern nur einmal speichert → True
-----------------------------------------------------------------------------------
"""
x = 'Peter'
y = 'Peter'
res = x is y       # True
print(res)

print(x < y)       # False
print(x != y)      # False
print(x is not y)  # False

print(id(x))  # e.g. 140539652049216
print(id(y))  # e.g. 140539652049216 (gleiche Speicheradresse)
