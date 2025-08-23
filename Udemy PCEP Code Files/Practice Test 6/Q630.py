"""
functions.py erstellen

functions → enthält einen String, der den Python-Code für die Funktion func() hält.
with open(..., 'w') as f: → öffnet die Datei functions.py im Schreibmodus (w = write).
f.write(functions) → schreibt den Code-String in die Datei.
--------------------------------------------------------------------------------------------
index.py erstellen

index → String, der den Code enthält, um functions.py zu importieren und func() auszuführen.
f.write(index) → schreibt diesen Code in die Datei index.py.
--------------------------------------------------------------------------------------------
Was passiert, wenn man index.py ausführt

Python importiert functions.py
Ruft functions.func() auf → Ausgabe:
--------------------------------------------------------------------------------------------
💡Merksätze für Anfänger:

Strings in Python können Python-Code enthalten, den man in Dateien schreiben kann.
open(..., 'w') überschreibt die Datei, wenn sie existiert.
Mit import kann man Code aus einer anderen Datei ausführen.
--------------------------------------------------------------------------------------------
"""



functions = '''
def func():
    print('Hello world')
'''
with open('functions.py', 'w') as f:
    f.write(functions)

index = '''
import functions
functions.func()
'''
with open('index.py', 'w') as f:
    f.write(index)
