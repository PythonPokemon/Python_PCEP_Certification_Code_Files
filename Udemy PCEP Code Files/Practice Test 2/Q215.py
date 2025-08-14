"""
1️⃣ Unterschied Liste vs. Dictionary
Liste
Hat Index-Positionen (0, 1, 2, …)
Zugriff über liste[0] → erstes Element
----------------------------------------------------------------------------------------------------
Dictionary
Hat Keys (Schlüssel) statt fester Indizes
Zugriff über dict[key]
Keine garantierte Reihenfolge (auch wenn in Python 3.7+ die Einfügereihenfolge beibehalten wird)


"""

people = {} #  leeres Dictionary.


def add_person(index):
    if index in people:
        people[index] += 1
    else:
        people[index] = 1

# fügt die daten hinzu
add_person('Peter')
add_person('Paul')
add_person('peter')

print(len(people))  # 3
print(people)       # {'Peter': 1, 'Paul': 1, 'peter': 1}


#--------------------------------------------------------------------------------
# BONUS

#print(people[0])    # KeyError: 0 | weil das der abruf bei einer Liste wäre!

# Test |  Falls du wirklich wie bei einer Liste "per Position" zugreifen willst:
print("Testaufruf Key Bassiert:")
keys = list(people.keys())  # ['Peter', 'Paul', 'peter']
print(people[keys[0]])      # Wert zu 'Peter'   == 1
print(people[keys[1]])      # Wert zu 'Paul'    == 1
print(people[keys[2]])      # Wert zu 'peter'   == 1
