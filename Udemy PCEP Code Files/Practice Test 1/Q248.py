"""
Frage 31
Übersprungen
Q248

Only one of the following statements is true - which one?

Richtige Antwort
multiplication precedes addition | Multiplikation geht der Addition voraus

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| Precedence (Reihenfolge) | Operator            | Description (EN)                                  | Beschreibung (DE)                                         | Associativity (Verknüpfungsrichtung) |
| ------------------------ | ------------------- | ------------------------------------------------- | --------------------------------------------------------- | ------------------------------------ |
| 1                        | `**`                | Exponentiation                                    | Potenzierung                                              | Right to left (rechts nach links)    |
| 2                        | `+x`, `-x`          | Positive, Negative (Unary)                        | Vorzeichen Plus, Vorzeichen Minus (unär)                  | Right to left (rechts nach links)    |
| 3                        | `*`, `/`, `%`, `//` | Multiplication, Division, Modulus, Floor division | Multiplikation, Division, Modulo (Rest), Ganzzahldivision | Left to right (links nach rechts)    |
| 4                        | `+`, `-`            | Addition, Subtraction                             | Addition, Subtraktion                                     | Left to right (links nach rechts)    |
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""


print(2 + 3 * 4)    # 14
print(2 + (3 * 4))  # 14
print(2 + 12)       # 14
print(14)           # 14
