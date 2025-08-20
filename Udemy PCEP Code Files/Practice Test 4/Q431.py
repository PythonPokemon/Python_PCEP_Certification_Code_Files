"""
Operator-Priorität in Python (vereinfacht)
-------------------------------------------------------------------------------------------------------
Von höchster zu niedrigster Priorität:
-------------------------------------------------------------------------------------------------------
Rang	    Operator(en)	        Beschreibung
-------------------------------------------------------------------------------------------------------
1	            ()	                Klammern → höchste Priorität
2	            **	                Potenzierung
3	        +x, -x, ~x	            Vorzeichen, Bit-Not
4	        *, /, //, %	            Multiplikation, Division, Ganzzahldivision, Modulo
5	            +, -	            Addition, Subtraktion
6	    >, <, >=, <=, ==, !=	    Vergleichsoperatoren
7	            and	                Logisches UND
8	            or	                Logisches ODER
-------------------------------------------------------------------------------------------------------
True ist ein boolescher Wert, aber Python behandelt True automatisch als 1 in numerischen Berechnungen.
False würde automatisch als 0 behandelt werden.
Berechnung
-------------------------------------------------------------------------------------------------------
Division zuerst (/ hat höhere Priorität als +)
3 / True   → 3 / 1 = 3.0
-------------------------------------------------------------------------------------------------------
Addition danach
7 + 3.0 → 10.0
-------------------------------------------------------------------------------------------------------
Warum das Ergebnis 10.0 ist
Division / in Python liefert immer einen float, auch wenn beide Operanden ganze Zahlen sind.
Daher: 3 / True = 3.0
Addition mit 7 → 7 + 3.0 = 10.0
-------------------------------------------------------------------------------------------------------
💡 Merksatz

Bool → int: True = 1, False = 0
Bei Division / wird immer ein float erzeugt
Operator-Priorität: * / // % vor + -
-------------------------------------------------------------------------------------------------------
"""


w = 7
x = 3
y = 4
z = True
a = w + x * y        # 7 + 3*4 | == 7 + 12 | == 19
b = w + x / z        # 7 + 3/1 | == 7 + 3.0 | == 10.0 | Achtung bei division wird int zu float
print(7 + 3 * 4)     # 19
print(7 + (3 * 4))   # 19
print(7 + 12)        # 19
print(a)             # 19
print(7 + 3 / True)  # 10.0 | True ist ein boolescher Wert, aber Python behandelt True automatisch als 1 in numerischen
print(7 + 3 / 1)     # 10.0
print(7 + (3 / 1))   # 10.0
print(7 + 3.0)       # 10.0
print(b)             # 10.0
print(a > b)         # True | 19 ist größer 10
print(a == b)        # False| 19 ist das gleiche wie 10 ! FALSCH 
print(a <= b)        # False| 19 ist kleiner gleich 10 ! FALSCH
print(a < b)         # False| 19 ist kleiner 10

if a > b:
    print('TRUE')    # TRUE
else:
    print('FALSE')
