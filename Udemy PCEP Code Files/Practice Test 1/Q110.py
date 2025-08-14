"""
1️⃣ Grundprinzip
In Python gilt:

"Leere" Werte werden zu False.
Nicht-leere Werte werden zu True.
Das betrifft Zahlen, Strings, Listen, Tupel, Dictionaries, Sets usw.
---------------------------------------------------------------------

4️⃣ Merksatz
🔹 "Leer" = False, "Gefüllt" = True
Das gilt egal, ob es sich um Zahlen, Zeichenketten, Listen oder andere Container handelt.

➡ Alle sind leer oder gleich Null → False.
"""


print(bool(23))       # True
print(bool(''))       # False
print(bool(' '))      # True
print(bool([False]))  # True

print()

print(bool(''))        # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(None))      # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(set()))     # False
print(bool(range(0)))  # False

# ➡ Alle sind leer oder gleich Null → False.