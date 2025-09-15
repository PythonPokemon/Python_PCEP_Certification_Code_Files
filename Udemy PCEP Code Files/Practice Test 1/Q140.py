"""
Frage 126
Übersprungen
Q140
isalnum() checks if a string contains only letters and digits, and this is:

Richtige Antwort
A method

Erklärung
The isalnum() method is a built-in method in Python that belongs to the string class. It is used to check if a string contains only alphanumeric characters (letters and digits). 
As a method, it is called on a string object using dot notation, such as "string.isalnum()".
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
.isalnum() in Python
True → wenn alle Zeichen alphanumerisch sind:
Buchstaben (A-Z, a-z)
Ziffern (0-9)

!!! False → wenn mindestens ein Zeichen kein Buchstabe oder keine Ziffer ist 
(z. B. Leerzeichen, Punkt, Komma, Sonderzeichen).
"""


print('James007'.isalnum())     # True → nur Buchstaben + Zahlen
print('Hello world'.isalnum())  # False  → enthält ein Leerzeichen
