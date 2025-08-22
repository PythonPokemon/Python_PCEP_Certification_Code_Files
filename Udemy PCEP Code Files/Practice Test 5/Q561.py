"""
iteriert bis zur gesuchten, zeichenkette
----------------------------------------
"""


for ch in "adam_smit@openedg.org":
    if ch == "@":
        break
    print(ch, end="")  # adam_smit
