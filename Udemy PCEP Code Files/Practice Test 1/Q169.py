"""
Frage 83
Übersprungen
Q169

How many stars (*) does the code output to the screen?
------------------------------------------------------
Richtige Antwort
three

"""


floor = 10
while floor != 0:
    floor //= 4
    print(floor, end="")  # 2 0
    print("*", end="")    # * *
else:
    print("*")            # *
