"""
Frage 19
Übersprungen
Q537
You have the following file.

index.py:
from sys import argv
print(argv[1] + argv[2])

You run the file by executing the following command in the terminal.
python index.py 42 3

What is the expected oputput?
Richtige Antwort
423
---------------------------------------------------------------------
argv[0] = Dateiname (index.py)
argv[1] = "42" (als String)
argv[2] = "3" (als String)

👉 Und print(argv[1] + argv[2]) bedeutet String-Konkatenation: 
"42" + "3" = "423".
Deshalb ist die richtige Antwort = 423 ✅
---------------------------------------------------------------------
"""

# First execute the following to create the needed file:
code = '''
from sys import argv
print(argv[1] + argv[2])
'''
with open('index.py', 'w') as f:
    f.write(code)

# In Terminal:
# python index.py 42 3
