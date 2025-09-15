"""
Frage 157
Übersprungen
Q644
A value returned by the input() function is:

Richtige Antwort
a string

Erklärung
The input() function in Python always returns a string, regardless of the type of input provided by the user. 
This is because Python treats all user inputs as strings by default, and it is up to the programmer to convert the input to the desired data type if needed.

"""


value = input("Put anything in!")
print(type(value))  # <class 'str'>
