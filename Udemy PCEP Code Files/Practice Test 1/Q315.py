"""
Frage 48
Übersprungen
Q315

You want to print each name of the list on a new line.

data = ['Peter', 'Paul', 'Mary', 'Jane']

Which statement will you use?
------------------------------------------------------
Richtige Antwort
print('\n'.join(data))
------------------------------------------------------
"""


data = ['Peter', 'Paul', 'Mary', 'Jane']
print('\n'.join(data))                  # data wird der funktion als argument

"""
Peter
Paul
Mary
Jane
"""

# print(data.join('\n'))           # AttributeError: ...
# print(data.concatenate('\n'))    # AttributeError: ...
# print(data.join('%s\n', names))  # AttributeError: ...
