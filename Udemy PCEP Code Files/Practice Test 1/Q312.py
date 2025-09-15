"""
Frage 39
Übersprungen
Q312

What is the expected output of the following code?
--------------------------------------------------
Richtige Antwort
x is 3 and y is 7 and z is 10
x is 42 and y is 23 and z is 24
x is 100 and y is 23 and z is 60
"""

def test(x, y=23, z=10):
    print('x is', x, 'and y is', y, 'and z is', z)

# es werden immer die zugewiesen genommen, der rest wie oben initialiseriert:(x, y=23, z=10)
test(3, 7)         # x is 3 and y is 7 and z is 10
test(42, z=24)     # x is 42 and y is 23 and z is 24
test(z=60, x=100)  # x is 100 and y is 23 and z is 60
