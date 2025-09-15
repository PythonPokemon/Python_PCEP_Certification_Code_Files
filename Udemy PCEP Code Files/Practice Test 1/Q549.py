"""
Frage 60
Übersprungen
Q549

What is the output of the following code?

my_list = [3, 1, -1]
my_list[-1] = my_list[-2]
print(my_list)
-----------------------------------------
Richtige Antwort
[3, 1, 1]
"""


my_list = [3, 6, -5]        # ob nun ein minus davor steht ist egal in diesem bsp. [3, 1, -1] oder so [3, 1, 1] 
print(my_list[-1])          # -5 
my_list[-1] = my_list[-2]   # Hier wird der Wert des vorletzten Elements in das letzte Element geschrieben der liste überschrieben
print(my_list)              # [3, 6, 6]


"""
Erklärung:

Der Index stellt das letzte Element dar.-1
Der Index stellt das vorletzte Element dar.-2

Hier wird der Wert des vorletzten Elements in das letzte Element geschrieben.
"""