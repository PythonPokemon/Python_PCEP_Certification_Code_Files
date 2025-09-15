"""
Frage 100
Übersprungen
Q514

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort

False
False
True
True
"""


nums = [3, 7, 23, 42]            # Liste mit Zahlen
alphas = ['p', 'p', 'm', 'j']    # Liste mit Strings

print(nums is alphas)            # False -> zwei verschiedene Objekte im Speicher
print(nums == alphas)            # False -> auch die Inhalte sind unterschiedlich

print(id(nums))                  # z.B. 140539383947452 (Speicheradresse von nums)
print(id(alphas))                # z.B. 140539383900864 (Speicheradresse von alphas, also anders)

nums = alphas                    # nums zeigt jetzt auf dasselbe Objekt wie alphas

print(nums is alphas)            # True -> beide Namen zeigen auf dasselbe Objekt
print(nums == alphas)            # True -> Inhalte sind gleich (identisch)

print(nums)                      # ['p', 'p', 'm', 'j']
print(alphas)                    # ['p', 'p', 'm', 'j']

print(id(nums))                  # z.B. 140539652049216
print(id(alphas))                # z.B. 140539652049216 (gleich -> gleiche Speicheradresse)
