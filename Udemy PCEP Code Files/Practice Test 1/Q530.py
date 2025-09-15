"""
Frage 10
Übersprungen
Q530

You create a function to calculate the power of a number by using Python.
You need to ensure that the function is documented with comments
You create the following code. Line numbers are included for reference only.

Which of the following statements are true?
Choose two.

Richtige Auswahl
Line 07 contains an inline comment.

Richtige Auswahl
Lines 01 through 04 will be ignored for syntax checking.
"""


# 1 The calc_power function calculates exponents
# 2 x is the base
# 3 y is the exponent
# 4 The value of x raised to the y power is returned
def calc_power(x, y):
    comment = "# Return the value"
    # 7 print(comment)  # '# Return the value'   | Line 07 contains an inline comment.
    return x ** y   # raise x to the y power


print(calc_power(2, 8))  # 256
