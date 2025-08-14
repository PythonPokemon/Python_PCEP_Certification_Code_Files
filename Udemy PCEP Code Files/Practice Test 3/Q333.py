"""
💡 Mini-Erklärung für Teilnehmer

„Mit with open(..., 'w') kann man nicht nur Textdateien schreiben, sondern auch komplette Python-Skripte automatisch erzeugen. 
Danach kann man sie wie normale Module importieren.“
"""

# datei erstellung 1.
functions = '''
def func():
    print('Hello world')
'''
with open('functions.py', 'w') as f:
    f.write(functions)

# Datei erstellung 2.
index = '''
import functions
functions.func()
'''
with open('index.py', 'w') as f:
    f.write(index)

