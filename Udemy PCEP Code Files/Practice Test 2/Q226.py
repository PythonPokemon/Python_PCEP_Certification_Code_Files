"""
Das nennt sich implizite String-Konkatenation.

🔹 Was passiert hier?
In Python kannst du zwei String-Literale direkt hintereinander schreiben, ohne +.
Python „klebt“ sie beim Parsen schon zusammen, bevor der Code überhaupt läuft.
"""


print('Peter' 'Wellert')  # PeterWellert

x = 'Hello' 'world'
print(x)  # Helloworld
