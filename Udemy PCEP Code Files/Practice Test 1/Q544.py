"""
--------------------------------------
Frage 35
Übersprungen
Q544

A keyword is a word:

(Select two answers)

Richtige Auswahl
that cannot be used as a function name

Richtige Auswahl
that cannot be used as a variable name
--------------------------------------
"""


import keyword
print(keyword.kwlist)

# Schlüsselwörter
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for','from', 'global', 'if',
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# bsp.
# for = 7 # SyntaxError: invalid syntax
# def for(): pass  # SyntaxError: invalid syntax