
"""
Erklärung der Schlüsselbegriffe
-------------------------------------------------------------------------------
try: → der Block, in dem Fehler (Exceptions) auftreten können
-------------------------------------------------------------------------------
raise Exception → wirf eine Exception vom Typ Exception
-------------------------------------------------------------------------------
except <Typ>: → fängt Exceptions des angegebenen Typs
-------------------------------------------------------------------------------
Reihenfolge der except-Blöcke ist wichtig: Python prüft sie von oben nach unten
-------------------------------------------------------------------------------
Typ-Hierarchie der Exceptions
BaseException
 └── Exception
      └── ...


BaseException ist die Oberklasse aller Exceptions
Exception ist eine Unterklasse von BaseException
Alle Exceptions, die Exception erben, werden auch von BaseException abgefangen
-------------------------------------------------------------------------------
"""
# SyntaxError: default 'except:' must be last


try:
    raise Exception
except BaseException:
    print("a")         # a
except Exception:
    print("b")
except:
    print("c")
