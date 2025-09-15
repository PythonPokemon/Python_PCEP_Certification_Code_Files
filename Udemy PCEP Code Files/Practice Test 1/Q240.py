"""
Frage 68
Übersprungen
Q240

You develop a Python application for your company.

A named contains 200 employee names,listemployees
the last five being company management.
You need to slice the to display all employees excluding management.list

Which code segments can you use?
Choose two.
------------------------------------------------------------------------
Richtige Auswahl
employees[0:-5]

Richtige Auswahl
employees[:-5]
------------------------------------------------------------------------
"""


employees = []

# for i in range(1, 196):
for i in range(1, 6): # Just for convenience
    employees.append('Employee' + str(i))

for i in range(1, 6):
    employees.append('Manager' + str(i))

print(employees)
print(employees[:-5])
print(employees[0:-5])
print(employees[1:-4])
# One manager present and one employee is missing
print(employees[1:-5])  # One employee is missing
print(employees[0:-4])  # One manager present
