"""
Frage 72
Übersprungen
Q203

What is the expected output of the following code?
------------------------------------------------------------------------------------------------
Richtige Antwort
[4, 3, 2]

Erklärung:
Aufteilen von Listen: [start(inclusive):end(exclusive):step]
Der Schritt ist hier negativ.
Dadurch kann der Slice von rechts nach links aufgebaut werden (Start wechselt sich mit Ende ab).
Der Anfang ist der Index (inklusive) und das Ende ist der Index (exklusiv).30
------------------------------------------------------------------------------------------------
"""

# Index:
#    |  |  |  |  |
#    0  1  2  3  4
a = [1, 2, 3, 4, 5]
print(a[3:0:-1])  # [4, 3, 2]
