"""
Frage 103
Übersprungen
Q165

Which of the approachable except: branches is taken into consideration when an exception occurs? | Welche der zugänglichen Zweige wird berücksichtigt, wenn eine Ausnahme auftritt?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Richtige Antwort
The first matching branch.

Erklärung
In Python, wenn eine Ausnahme auftritt, durchläuft der Interpreter jede except: 
Branche in der Reihenfolge, in der sie im Code definiert sind. Der erste passende Zweig, der die spezifische Ausnahme behandeln kann, wird ausgeführt, 
und der Interpreter überprüft nicht weiter die verbleibenden Zweige. 
Das bedeutet, dass der erste passende Zweig derjenige ist, der in Betracht gezogen wird, wenn eine Ausnahme auftritt.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


try:
    zahl = 100 / 0
except ArithmeticError:
    print('ArithmeticError')  # ArithmeticError
except ZeroDivisionError:
    print('ZeroDivisionError')

try:
    zahl = 100 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')  # ZeroDivisionError
except ArithmeticError:
    print('ArithmeticError')

print(issubclass(ZeroDivisionError, ArithmeticError))  # True
