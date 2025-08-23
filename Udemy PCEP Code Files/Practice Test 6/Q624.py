"""
Primzahlen :-()

Das ist ein klassischer Primzahl-Algorithmus mit einer Trial Division (Teilen durch alle kleineren Zahlen).
"""


num = 2                         # Die Variable num startet bei 2, weil 1 keine Primzahl ist.
while num <= 100:               # Die Schleife läuft, solange num kleiner oder gleich 100 ist.
    is_prime = True             # Zu Beginn nehmen wir an, dass die aktuelle Zahl num eine Primzahl ist.
    for i in range(2, num):     # Prüft alle Zahlen i von 2 bis num-1, ob sie num teilen können.
        if num % i == 0:        # Falls num durch i teilbar ist (Rest = 0), ist sie keine Primzahl.
            is_prime = False    # is_prime wird auf False gesetzt.
            break               # Mit break wird die innere Schleife sofort abgebrochen
    if is_prime == True:        # Wenn keine Teilbarkeit gefunden wurde (is_prime bleibt True), ist num eine Primzahl und wird ausgegeben.
        print(num)              # 2 -> 3 -> 5 -> ... -> 89 -> 97 | es werden alle Primzahlen ausgegeben!
    num += 1                    # Nach jeder Überprüfung wird num um 1 erhöht → nächste Zahl prüfen.

print('----------')

num = 2
is_prime = True                 # außerhalb der schleife
while num <= 100:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(num)              # 2 -> 3 | hört nach der ersten Primzahl auf
    num += 1

print('----------')

num = 2
while num <= 100:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime == False:       # auf false statt true wie zuvor
        print(num)              # 4 -> 6 -> 8 -> ... -> 99 -> 100
    num += 1

print('----------')

# stop = 0  # Just added to prevent the infinite loop

# num = 2
# while num <= 100:
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime == True:
#         print(num)  # 2 -> 2 -> 2 -> ... -> 2 -> 2

#     stop += 1
#     # Just added to prevent the infinite loop
#     if stop > 100:
#         break
#     # Just added to prevent the infinite loop
