"""
Frage 122
Übersprungen
Q454
A way of passing arguments in which the order of the arguments determines the initial parameter's values is referred to as:?

Richtige Antwort
positional
"""


def my_function(a, b):
    print(a, b)


my_function('Hello', 'World')  # Hello World
my_function('World', 'Hello')  # World Hello
