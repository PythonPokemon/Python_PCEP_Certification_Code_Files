"""
Frage 74
Übersprungen
Q507

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
one
"""


data = {'one': 'two', 'two': 'three', 'three': 'one'}   # dictionary
res = data['three']                                     # variable res bekommtvon der variable data nur den key 'three' zugewiesen, das den wert 'one' enthält!

for _ in range(len(data)):
    res = data[res]

print(res)  # one
