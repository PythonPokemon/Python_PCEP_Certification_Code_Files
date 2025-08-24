"""
💡 Merksatz:

global = Zugriff und Modifikation einer Variablen außerhalb der Funktion
Ohne global → Zuweisung erstellt lokale Variable im Funktionsscope
------------------------------------------------------------------------
1. x: 42
2. x: 23
3. x: 23
"""

x = 42
print(id(x))            # 140703694735560


def func():
    global x            # zugriff innerhalb der funktion/methode auf die äußere variable oben x == 42
    print(id(x))        # 140703694735560 (deshalb auch gleiche speicheradresse)
    print('1. x:', x)
    x = 23              # nachdem die Globale variable in der funktion aufrgerufen und einen neuen wert bekommt
    print('2. x:', x)   # ändert sich auch die speicheradresse
    print(id(x))        # 140704560072296

func()
print('3. x:', x)

