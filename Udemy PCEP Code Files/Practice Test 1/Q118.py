"""
Frage 112
Übersprungen
Q118

How many stars will the following snippet print to the monitor?
---------------------------------------------------------------
Richtige Antwort
1
"""

i = 4
while i > 0:    # i ist 4
    i -= 2      # i 4 - 2 == ist 2
    print('*')  # *
    if i == 2:  # Y, i ist 2
        break   # verlasse die Schleife
else:           # der rest wird nicht ausgeführt, wenn die Schleife verlassen wird!
    print('*')

