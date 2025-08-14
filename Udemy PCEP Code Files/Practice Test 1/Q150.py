"""
Kurzfassung
Tupel sind immutable (unveränderlich).
Du kannst ihre Werte nicht direkt ändern.
Um Werte zu „ändern“, musst du eine neue Variable erzeugen oder das Tupel in eine Liste konvertieren.

"""


my_tuple = (1, 2, 3)
my_tuple[1] = my_tuple[1] + my_tuple[0]
# TypeError
