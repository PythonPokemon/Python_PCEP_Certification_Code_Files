"""
1️⃣ Variante mit print in der Funktion

def func():
    print('Hello world')

Zweck: Sofort etwas auf den Bildschirm schreiben.
Nachteil: Der Wert ist „verbraucht“, du kannst ihn nicht weiterverarbeiten.
Rückgabewert: None (wenn kein return da ist, fügt Python automatisch return None ein).
-----------------------------------------------------------------------------------------
2️⃣ Variante mit return

def func2():
    return 'gibt den rückgabewert aus!'

Zweck: Die Funktion liefert einen Wert zurück.
Vorteil: Du kannst ihn:
    drucken (print(func2()))
    in einer Variablen speichern (text = func2())
    in anderen Funktionen weiterverwenden
-------------------------------------------------------------------------------------------
| ----------------------- | ------------------- | --------------------------------------- |
| Merkmal                 | `print` in Funktion | `return` in Funktion                    |
| ----------------------- | ------------------- | --------------------------------------- |
| **Sichtbar in Konsole** | Sofort beim Aufruf  | Nur, wenn extra `print(...)` drum herum |
| **Weiterverwendbar**    |  Nein               |     Ja                                  |
| **Rückgabewert**        | `None`              | Der angegebene Wert                     |
| ----------------------- | ------------------- | --------------------------------------- |
                                ❌ Nein	                    ✅ Ja                       |
-------------------------------------------------------------------------------------------
💡 Merksatz für Teilnehmer

„print ist wie sprechen - man hört es sofort, aber man kann es nicht wiederverwenden.
return ist wie einen Zettel schreiben - man gibt die Information zurück, damit jemand anderes sie nutzen kann.“
"""


def func():
    print('Hello world')

func()           # funktionsaufruf | führt print('Hello world') aus → Ausgabe: Hello world
print(func())    # print führt func() aus → gibt Hello world aus, 
                 # dann druckt print(...) den Rückgabewert (None)

print('-----------')

def func2():
    return('gibt den rückgabewert aus!')

print(func2())