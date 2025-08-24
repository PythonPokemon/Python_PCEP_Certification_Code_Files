"""
Modulo Operator %

Prüft, ob x gerade ist (x % 2 == 0)
Wenn gerade → return 1
Wenn ungerade → return None (weil return ohne Wert None zurückgibt)
-------------------------------------------------------------------
Schrittweise:

Innerer Aufruf: func(2)

2 ist gerade → return 1
Also: func(2) = 1
-------------------------------------------------------------------
Äußerer Aufruf: func(1)

1 ist ungerade → return None
Also: func(func(2)) = None
-------------------------------------------------------------------
Addition: None + 1

None ist kein Zahlentyp → Python kann nicht addieren
→ TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
-------------------------------------------------------------------
Zusammenfassung

TypeError entsteht, weil die Funktion manchmal None zurückgibt
Addition mit None ist nicht erlaubt
-------------------------------------------------------------------
"""

def func(x):
    if x % 2 == 0:
        return 1            # wenn gerade rest 1
    else:
        return              # wenn ungerade == None

print(func(func(2)))        # gibt 'None' aus! | weil 2 / 2 == 0 rest 0
print(func(func(2)) + 1)    # TypeError: ...
