"""
Schritt-für-Schritt
-----------------------------------------------------------------------------------------------------
type(expr)

    Python führt die Operation zuerst aus, um den Typ des Ergebnisses zu bestimmen
    Beispiel:   23 + 42     → Ergebnis = 65 → type(65)              = <class 'int'>
    Beispiel: '23' + '42'   → Ergebnis = '2342' → type('2342')      = <class 'str'>
    Beispiel: '23' * 7      → Ergebnis = '23232323232323'           = <class 'str'>
-----------------------------------------------------------------------------------------------------
Operationen werden also nicht ignoriert, sie werden normal ausgeführt, bevor type() den Typ bestimmt.
-----------------------------------------------------------------------------------------------------
| Ausdruck      | Ergebnis         | type()          |
| ------------- | ---------------- | --------------- |
| `23 + 42`     | 65               | `<class 'int'>` |
| `'23' + '42'` | '2342'           | `<class 'str'>` |
| `'23' * 7`    | '23232323232323' | `<class 'str'>` |

-----------------------------------------------------------------------------------------------------
"""


print(type(23 + 42))      # <class 'int'>
print(type('23' + '42'))  # <class 'str'>
print(type('23' * 7))     # <class 'str'>
print(23 + 42)            # 65
print('23' + '42')        # 2342
print('23' * 7)           # 23232323232323
