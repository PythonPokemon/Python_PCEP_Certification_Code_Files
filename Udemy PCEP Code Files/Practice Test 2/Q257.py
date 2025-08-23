"""

In Python kannst du * nicht auf None anwenden.
Nur Zahlen, Strings, Listen usw. kennen eine Multiplikation.
---------------------------------------------------------------------------------------
✅ Fazit:

None ist kein Wert, mit dem man rechnen kann.
Wenn du in einer Funktion nichts zurückgibst oder explizit return None schreibst, 
dann bekommst du None als Ergebnis.
Versuchst du dann, mit None zu rechnen (+, -, *, /), bekommst du immer einen TypeError.
---------------------------------------------------------------------------------------
"""

# 👉 Egal, welchen Wert du a gibst, diese Funktion gibt immer None zurück.
                    # Das bedeutet:
def function_1(a):  #  # None
    return None


def function_2(a):
    return function_1(a) * function_1(a)    # macht keinen sinn nontype zu multiplizieren
    # TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'


print(function_2(2))

print(None * None)
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
