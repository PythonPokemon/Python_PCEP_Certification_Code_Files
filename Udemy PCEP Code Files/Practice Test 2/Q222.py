"""
Warum der SyntaxError bei:
print(len('\'))

Ein Backslash \ leitet in Python eine Escape-Sequenz ein (z. B. \n für Zeilenumbruch).
Wenn du nur einen Backslash am Ende schreibst, erwartet Python danach noch ein Zeichen, das „escaped“ werden soll → deshalb SyntaxError.


"""
# print(len('\'))    # SyntaxError: ...
print(len('\\'))     # 1 zeichen
# print(len('\\\'))  # SyntaxError: ...
print(len('\\\\'))   # 2 zeichen
