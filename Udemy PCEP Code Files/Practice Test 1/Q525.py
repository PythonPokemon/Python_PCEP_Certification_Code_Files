"""
Frage 105
Übersprungen
Q525

The following is a program to validate customer numbers.
The number may only contain numbers and dashes.

The number must have the right format (dd-ddd-dddd).

What is true about this program?
----------------------------------------------------------------------
Richtige Antwort
The program works properly. | Das Programm funktioniert ordnungsgemäß.
"""


customer_number = input('Enter the employee number (dd-ddd-dddd): ')          # Eingabe einer Nummer
customer_number = '12-345-6789'                                               # Testwert, soll True ergeben

parts = customer_number.split('-')                                            # Zerlegen am '-' -> ['12','345','6789']
valid = False                                                                 # Startwert: noch nicht gültig

if len(parts) == 3:                                                           # Prüfen: genau 3 Teile?
    if len(parts[0]) == 2 and len(parts[1]) == 3 and len(parts[2]) == 4:      # Länge: 2-3-4 Ziffern?
        if parts[0].isdigit() and parts[1].isdigit() and parts[2].isdigit():  # Sind alle Teile Zahlen?
            valid = True                                                      # Wenn ja -> gültig

print(valid)                                                                  # Ausgabe: True



