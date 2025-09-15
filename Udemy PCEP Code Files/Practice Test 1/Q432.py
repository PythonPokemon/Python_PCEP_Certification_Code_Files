"""
Frage 37
Übersprungen
Q432

What is the expected output of the following code?

print(not 0)
print(not 23)
print(not '')
print(not 'Peter')
print(not None)
---------------------------------------------------
Richtige Antwort
True
False
True
False
True
"""

# not ist gegenteil von wahr operator,
print(not 0)        # True
print(not 23)       # False
print(not '')       # True | bestes bsp. ist leer == eigentlich false aber weil es gegenteil ist == True!
print(not 'Peter')  # False
print(not None)     # True

print(bool(''))        # False
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False
print(bool(None))      # False
print(bool([]))        # False
print(bool(()))        # False
print(bool({}))        # False
print(bool(set()))     # False
print(bool(range(0)))  # False
