"""
division durch null ist nicht erlaubt.
"""

try:
    print(7 / 0)
except (TypeError, ValueError, ZeroDivisionError):
    print("That is not allowed!")

