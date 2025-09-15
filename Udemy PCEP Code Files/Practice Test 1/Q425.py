"""
Frage 140
Übersprungen
Q425
What is the default value of encoding in the string function encode()?

Richtige Antwort
utf-8

Erklärung
The default encoding value in the string function encode() is utf-8. This encoding is widely used and supports a wide range of characters, making it a common choice for encoding text data.

"""


print(list('a'.encode()))          # [97]
print(list('a'.encode('utf-8')))   # [97]
print(list('a'.encode('utf-16')))  # [255, 254, 97, 0]
print(list('a'.encode('utf-32')))  # [255, 254, 0, 0, 97, 0, 0, 0]
