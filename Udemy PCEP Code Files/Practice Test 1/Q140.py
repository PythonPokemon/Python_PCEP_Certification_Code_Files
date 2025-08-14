"""
.isalnum() in Python
True → wenn alle Zeichen alphanumerisch sind:
Buchstaben (A-Z, a-z)
Ziffern (0-9)

!!! False → wenn mindestens ein Zeichen kein Buchstabe oder keine Ziffer ist 
(z. B. Leerzeichen, Punkt, Komma, Sonderzeichen).
"""


print('James007'.isalnum())     # True → nur Buchstaben + Zahlen
print('Hello world'.isalnum())  # False  → enthält ein Leerzeichen
