"""
Frage 132
Übersprungen
Q457
Select the true statements:
(Select two answers)


Richtige Auswahl
You cannot use keywords as function names in Python

Richtige Auswahl
You cannot use keywords as variable names in Python
"""

# for = 7 # SyntaxError: invalid syntax
# def for(): pass  # SyntaxError: invalid syntax

import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
 'else', 'except', 'finally', 'for','from', 'global', 'if',
 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
