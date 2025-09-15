"""
Frage 52
Übersprungen
Q223

What is the expected output of the following code?

x = """
"""
print(len(x))
--------------------------------------------------
Richtige Antwort
1
"""

# Jeder zeilenumbruch wird als ein leerzeichen oder auch string gewertet!
x = """
"""
print(len(x))  # 1

# ord() returns an integer representing the Unicode character.
print(ord(x[0]))  # 10 (LF: line feed, new line)

# Gleiches Ergebnis mit einfachen Anführungszeichen:
y = '''
'''
print(len(y))  # 1

# 2x Zeilenumbruch == 2 Leerzeichen:
z = """

"""
print(len(z))  # 2
