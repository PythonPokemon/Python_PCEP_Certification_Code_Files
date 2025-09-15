"""
Frage 92
Übersprungen
Q322

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
2
"""


data = (1, 2, 4, 8)
data = data[1:-1]   # weist der varibale nur die expliziten werte aus dem slicing mit == index 1 ist 2 und das letzte element von rechts exclusiv 4 == 2 4
print(data)         # (2, 4)
data = data[0]      # weist der varibale data erneut einen wert auf index zu == 2!
print(data)         # 2 | Achtung einzieges element!
