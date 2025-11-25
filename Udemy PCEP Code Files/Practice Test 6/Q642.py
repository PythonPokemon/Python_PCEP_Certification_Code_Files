"""
Erklärung:

s = 'python' → s ist ein String, und Strings sind immutable (unveränderlich) in Python.
In der Schleife:

i = s[i].upper()

---------------------------------------------------------------------------------------
passiert folgendes:

s[i] ist ein einzelnes Zeichen, z. B. 'p'.
.upper() macht daraus 'P'.

Dieses Ergebnis wird aber nur der Variablen i zugewiesen
und s selbst bleibt unverändert.
Darum bleibt am Ende s = "python".
---------------------------------------------------------------------------------------
👉 Fazit: Dein Code verändert nicht den String, 
sondern überschreibt nur die Schleifenvariable i.
Deshalb bleibt das Ergebnis python.
---------------------------------------------------------------------------------------
Wenn du den String in Großbuchstaben haben möchtest:
---------------------------------------------------------------------------------------
Variante 1 (direkt mit .upper()):

s = 'python'
print(s.upper())   # PYTHON
---------------------------------------------------------------------------------------
Variante 2 (Schleife, Zeichenweise neu zusammensetzen):

s = 'python'
neuer_string = ""

for i in range(len(s)):
    neuer_string += s[i].upper()

print(neuer_string)   # PYTHON
---------------------------------------------------------------------------------------
"""


s = 'python'    # länge 6
for i in range(len(s)):
    i = s[i].upper()
    # s[i] = s[i].upper()  # TypeError: ...
print(s, end="")           # python

