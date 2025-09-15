"""
Frage 164
Übersprungen
Q150
Assuming that the tuple is a correctly created tuple, the fact that tuples are immutable means that the following instruction:

my_tuple[1] = my_tuple[1] + my_tuple[0] 
---------------------------------------

Richtige Antwort
is illegal
---------------------------------------------
Kurzfassung
Tupel sind immutable (unveränderlich).
Du kannst ihre Werte nicht direkt ändern.
Um Werte zu „ändern“, musst du eine neue Variable erzeugen oder das Tupel in eine Liste konvertieren.

"""


my_tuple = (1, 2, 3)
my_tuple[1] = my_tuple[1] + my_tuple[0]
# TypeError
