"""
Frage 243
Übersprungen
Q355

The meaning of the keyword parameter is determined by:



its connection with existing variables

its position within the argument list

its value

Richtige Antwort
the argument's name specified along with its value
"""


def my_function(b=7, a=11):
    print(a, b)


# The argument's name determines the keyword parameter:
my_function(b=1, a=2)  # 2 1

# With keyword parameters the values do not matter:
my_function(11, 7)  # 7 11

# With keyword parameters the postion
# within the argument list does not matter:
my_function(a=1, b=2)  # 1 2

# Keyword parameters do not connect with existing variables:
a = 23; b = 42
my_function(a, b)  # 42 23
