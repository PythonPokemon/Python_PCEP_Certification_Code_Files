"""
\' → erlaubt, ein einzelnes ' innerhalb von einfachen Anführungszeichen '...' zu verwenden
\" → erlaubt, ein doppeltes " innerhalb von '...' zu verwenden
Ohne \ würde Python denken, dass die Zeichenkette an diesem ' oder '"' endet, und es gäbe einen Syntaxfehler.
-------------------------------------------------------------------------------------------------------------
💡 Merksatz

\ = Escape-Zeichen → ermöglicht Sonderzeichen im String
Praktisch für ', ", \n (Zeilenumbruch), \t (Tab) usw.
-------------------------------------------------------------------------------------------------------------
"""


print("Peter's sister's name's \"Anna\"")
# Peter's sister's name's "Anna"
print('Peter\'s sister\'s name\'s \"Anna\"')    # bei einzelnen anführungszeichen würde es zu syntaxError führen, ohne backslashes \
# Peter's sister's name's "Anna"
# print("Peter's sister's name's "Anna"")
# SyntaxError: invalid syntax
# print('Peter's sister's name's "Anna"')
# SyntaxError: invalid syntax
