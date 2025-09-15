"""
---------------------------------------------------------------------
Frage 40
Übersprungen
Q528

You have the following file.

You want the following output?
The average score for Peter is 200.00
Which command do you have to execute in the command line?
---------------------------------------------------------------------
Richtige Antwort
python index.py Peter 100 200 300
---------------------------------------------------------------------
| Index    | Wert       | Bedeutung                   |
| -------- | ---------- | --------------------------- |
| argv\[0] | 'index.py' | Name des Skripts            |
| argv\[1] | 'Paul'     | Name der Person             |
| argv\[2] | '100'      | Erste Zahl für Durchschnitt |
| argv\[3] | '200'      | Zweite Zahl                 |
| argv\[4] | '300'      | Dritte Zahl                 |
---------------------------------------------------------------------
range(2, len(argv)) → startet bei Index 2
Addiert also: argv[2] + argv[3] + argv[4] → 100 + 200 + 300 sum = 600
---------------------------------------------------------------------
len(argv) = 5
len(argv) - 2 = 3 → Anzahl der Zahlen
Durchschnitt: 600 / 3 = 200.0
"""


# First execute the following to create the needed file:
code = '''
from sys import argv
sum = 0
for i in range(2, len(argv)):
    sum += float(argv[i])
print(

    "The average score for {0} is {1:.2f}"

    .format(argv[1], sum/(len(argv)-2))
)
'''
with open('index.py', 'w') as f:
    f.write(code)

# In Terminal:
# py index.py Paul 100 200 300

