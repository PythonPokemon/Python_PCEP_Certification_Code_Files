"""
Python prüft die Blöcke der Reihe nach
Exception ist eine Unterklasse von BaseException
Der erste Block except BaseException fängt die Exception bereits ab → print('1') wird ausgeführt
Die anderen except-Blöcke werden nicht mehr geprüft
------------------------------------------------------------------------------------------------
Zusammenfassung

except prüft von oben nach unten
Unterklassen werden vom ersten passenden Block gefangen
Exception ist eine Unterklasse von BaseException, deshalb wird print('1') ausgegeben
except: am Ende wird nur erreicht, wenn vorher kein Block passt
------------------------------------------------------------------------------------------------
"""


try:
    raise Exception     # Wir erzeugen absichtlich eine Exception
except BaseException:   # Oberste Klasse fängt alles ab
    print('1')
except Exception:       # Subklasse von: BaseException
    print('2')
except:
    print('3')

print(issubclass(Exception, BaseException))     # Prüft, ob Exception eine Unterklasse von BaseException ist
                                                # Ergebnis: True, deshalb greift der erste except-Block


""" 
vereinfachte Hierarchie der wichtigsten Exceptions in Python
------------------------------------------------------------------------------------------------
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    ├── TypeError
    ├── NameError
    │   └── UnboundLocalError
    └── OSError
        ├── FileNotFoundError
        ├── PermissionError
        └── etc.
------------------------------------------------------------------------------------------------
"""