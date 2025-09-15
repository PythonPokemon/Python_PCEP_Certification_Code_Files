"""
Frage 117
Übersprungen
Q124

Which of the following variable names is illegal?



In

IN

in_

Richtige Antwort
in  
"""

# in = 'Hello'  # SyntaxError: invalid syntax == weil schlüsselwort
# in ist ein Schlüsselwort in Python

print(4 in [1, 4, 7, 11])  # True, weil 7 in der Liste enthalten ist, es wird also geprüft, ob 7 in der Liste enthalten ist

# Those work because python is case sensitiv
In = 'Hello'
IN = 'Hello'

# This one works because the underscore
# is a valid character for naming variables:
in_ = 'Hello'

import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async',
'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
'else', 'except', 'finally', 'for', 'from', 'global', 'if',
'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
