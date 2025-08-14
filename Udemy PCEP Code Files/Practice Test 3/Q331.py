"""
💡 Mini-Erklärung für Teilnehmer

„argv ist wie eine kleine Einkaufsliste der Befehlszeilenargumente. 
Das erste Element ist immer der Name der Datei, alle weiteren sind die zusätzlichen Wörter, die du beim Start mitgibst.
"""



# führe erst den import aus, in klammern!
code = '''
from sys import argv
print(argv[0])
'''
with open('index.py', 'w') as f:
    f.write(code)


