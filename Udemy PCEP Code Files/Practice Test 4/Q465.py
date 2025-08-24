
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


try:                    # der Block, in dem Fehler (Exceptions) auftreten können
    raise Exception     # wirft eine Exception vom Typ Exception
except BaseException:   # fängt Exceptions des angegebenen Typs BaseException
    print("a")          # a
except Exception:
    print("b")
except:
    print("c")

"""

-------------------------------------------------------------------------------
BaseException                               <---
 ├── SystemExit
 ├── KeyboardInterrupt
 ├── GeneratorExit
 └── Exception                              <---
      ├── StopIteration
      ├── StopAsyncIteration
      ├── ArithmeticError                   <---
      │    ├── FloatingPointError
      │    ├── OverflowError
      │    └── ZeroDivisionError
      ├── AssertionError                    <---
      ├── AttributeError
      ├── BufferError
      ├── EOFError
      ├── ImportError
      │    └── ModuleNotFoundError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── MemoryError
      ├── NameError
      │    └── UnboundLocalError
      ├── OSError
      │    ├── BlockingIOError
      │    ├── ChildProcessError
      │    ├── ConnectionError
      │    │    ├── BrokenPipeError
      │    │    ├── ConnectionAbortedError
      │    │    ├── ConnectionRefusedError
      │    │    └── ConnectionResetError
      │    ├── FileExistsError
      │    ├── FileNotFoundError
      │    ├── InterruptedError
      │    ├── IsADirectoryError
      │    ├── NotADirectoryError
      │    ├── PermissionError
      │    ├── ProcessLookupError
      │    └── TimeoutError
      ├── ReferenceError
      ├── RuntimeError
      │    ├── NotImplementedError
      │    ├── RecursionError
      │    └── FutureWarning
      ├── SyntaxError
      │    └── IndentationError
      │         └── TabError
      ├── SystemError
      ├── TypeError                         <---
      ├── ValueError
      │    └── UnicodeError
      │         ├── UnicodeDecodeError
      │         ├── UnicodeEncodeError
      │         └── UnicodeTranslateError
      ├── Warning
           ├── DeprecationWarning
           ├── PendingDeprecationWarning
           ├── RuntimeWarning
           ├── SyntaxWarning
           ├── UserWarning
           ├── FutureWarning
           ├── ImportWarning
           ├── UnicodeWarning
           └── ResourceWarning
----------------------------------------------------------------------------------
✅ Merksatz:

BaseException ist die Wurzel aller Fehler.
Exception ist die Wurzel aller „normalen“ Fehler, die man typischerweise abfängt.
Alles andere wie SystemExit, KeyboardInterrupt leitet direkt von BaseException ab, 
weil man die meist nicht zufällig mit except Exception: abfangen soll.
----------------------------------------------------------------------------------
"""