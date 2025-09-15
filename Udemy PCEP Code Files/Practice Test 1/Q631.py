"""
Frage 51
Übersprungen
Q631

You execute the following command in the terminal.

python index.py Hello

You want the command to print out Hello

What has to be inside of index.py?
--------------------------------------------------
Richtige Antwort
from sys import argv
print(argv[1])
--------------------------------------------------
argv
kommt aus dem Modul sys → from sys import argv
steht für argument vector

ist eine Liste aller Kommandozeilen-Argumente, 
die beim Start des Skripts übergeben wurden.

argv[0] = Dateiname (z. B. index.py)
argv[1] = erstes Argument
argv[2] = zweites Argument usw.
--------------------------------------------------
"""


# First execute the following to create the needed file:
code = '''
from sys import argv
print(argv[1])
'''
with open('index.py', 'w') as f:
    f.write(code)

# In Terminal:
# python index.py Hello
