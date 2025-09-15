"""
Frage 77
Übersprungen
Q427

The user enters 123

Which of the following code snippets will print to the monitor? 124
(Choose three.)
-------------------------------------------------------------------
Richtige Auswahl
num = int(input('Please enter your number: '))
print(num + 1)

Richtige Auswahl
num = input('Please enter your number: ')
print(int(num) + 1)

Richtige Auswahl
num = eval(input('Please enter your number: '))
print(num + 1)
-------------------------------------------------------------------
"""


# num = eval(input('Please enter your number: '))
num = eval('123')
print(num + 1)       # 124

# num = int(input('Please enter your number: '))
num = int('123')
print(num + 1)       # 124

# num = input('Please enter your number: ')
num = '123'
print(int(num) + 1)  # 124

# num = input('Please enter your number: ')
# print(num + 1)     # TypeError: ...
