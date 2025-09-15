"""
Frage 113
Übersprungen
Q110

Consider the following code snippet:
w = bool(23)
x = bool('')
y = bool(' ')
z = bool([False])


Which of the variables will contain False?
---------------------------------------------------------------------
Richtige Antwort
x
---------------------------------------------------------------------
1️⃣ Grundprinzip
In Python gilt:

"Leere" Werte werden zu False.
Nicht-leere Werte werden zu True.
Das betrifft Zahlen, Strings, Listen, Tupel, Dictionaries, Sets usw.
---------------------------------------------------------------------

4️⃣ Merksatz
🔹 "Leer" = False, "Gefüllt" = True
Das gilt egal, ob es sich um Zahlen, Zeichenketten, 
Listen oder andere Container handelt.

➡ Alle sind leer oder gleich Null → False.
"""
w = bool(23)            # befüllt → True
x = bool('')            # leer → False
y = bool(' ')           # befüllt (enthält ein Leerzeichen) → True
z = bool([False])       # befüllt (enthält ein Element) → True

print(bool(23))         # True
print(bool(''))         # False
print(bool(' '))        # True
print(bool([False]))    # True

print()

print(bool(''))         # False
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(0j))         # False
print(bool(None))       # False
print(bool([]))         # False
print(bool(()))         # False
print(bool({}))         # False
print(bool(set()))      # False
print(bool(range(0)))   # False

# ➡ Alle sind leer oder gleich Null → False.