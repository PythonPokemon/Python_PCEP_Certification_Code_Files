"""
Änderungen:

get_name → hole_name
calc_calories → berechne_kalorien
miles → kilometer
calories_per_mile → kalorien_pro_km
distance → strecke
burn_rate → kalorienrate
biker → fahrer
calories_burned → verbrauchte_kalorien

Kommentare auf Deutsch
Zahlenbeispiel angepasst, weil wir von Meilen auf Kilometer umgestellt haben
----------------------------------------------------------------------------------------
💡 Mini-Erklärung für Teilnehmer

„Die Funktion hole_name() fragt nach dem Namen und gibt ihn zurück.
Die Funktion berechne_kalorien() rechnet Strecke × Kalorienrate pro Kilometer.
Am Ende geben wir den Namen und den berechneten Kalorienverbrauch aus.“
"""


def get_name():
    # name = input('What is your name? ')
    name = 'Peter'
    return name


def calc_calories(miles, calories_per_mile):
    calories = miles * calories_per_mile
    return calories


# distance = int(input('How many miles did you bike this week? '))
distance = int('500')
burn_rate = 50
biker = get_name()
calories_burned = calc_calories(distance, burn_rate)
print(biker + ', you burned about', calories_burned, 'calories.')
# Peter, you burned about 37000 calories.
