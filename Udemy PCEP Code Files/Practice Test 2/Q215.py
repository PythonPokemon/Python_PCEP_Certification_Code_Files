people = {}   # 👉 Leeres Dictionary. Noch keine Einträge vorhanden.


def add_person(index):
    # 👉 Prüft: Gibt es den Schlüssel 'index' bereits im Dictionary people?
    if index in people:
        # 👉 Falls JA: Erhöhe den Zähler um 1.
        # Beispiel: aus {'Peter': 1} wird {'Peter': 2}
        people[index] += 1
    else:
        # 👉 Falls NEIN: Lege den Schlüssel mit dem Startwert 1 an.
        # Beispiel: people['Peter'] = 1
        people[index] = 1


# 👉 Nun rufen wir die Funktion drei Mal auf und übergeben jeweils einen String.
add_person("Peter")   # index = "Peter"  → neuer Eintrag → {'Peter': 1}
add_person('Paul')    # index = "Paul"   → neuer Eintrag → {'Peter': 1, 'Paul': 1}
add_person('peter')   # index = "peter"  → neuer Eintrag → {'Peter': 1, 'Paul': 1, 'peter': 1}
                      # WICHTIG: 'Peter' ≠ 'peter' (wegen Groß-/Kleinschreibung)


print(len(people))  # 👉 Anzahl der Einträge im Dictionary → 3

print(people)       # 👉 Ausgabe des gesamten Dictionaries:
                    # {'Peter': 1, 'Paul': 1, 'peter': 1}
