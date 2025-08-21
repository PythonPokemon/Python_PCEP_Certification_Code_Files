"""
1️⃣ Grundidee von assert

assert ist ein Debugging-Hilfsmittel, um sicherzustellen, dass eine Bedingung wahr ist.
Syntax:

assert <Bedingung>, <optional: Fehlermeldung>
Wenn <Bedingung> True → passiert nichts, Programm läuft weiter.
Wenn <Bedingung> False → es wird ein AssertionError ausgelöst → Programm stoppt.
"""


x = 0
assert x == 0
print('Hello')  # Hello

x = 7
assert x == 0  # AssertionError
print('Hello')

