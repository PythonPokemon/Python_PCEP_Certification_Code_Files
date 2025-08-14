"""
Achtung fehler, da die wert zuweisung ein string ist, teste mit int!

    value = "100"   falsch
    value = 100     korrekt
"""

try:
    value = "100"                   
    print(value/value)      # deivisions operation
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
    # Very very bad input...
except:
    print("Booo!")
