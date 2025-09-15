"""
Frage 56
Übersprungen
Q532

You want to print the sum of two number.
What snippet would you insert in the line indicated below:

x = input('Enter the first number: ')
y = input('Enter the second number: ')
#  insert your code here
----------------------------------------------------------
Richtige Antwort
print('The Result is ' + str(int(x) + int(y)))
----------------------------------------------------------
"""

x, y = '7', '11'  # Just for convenience

# You cannot concatenate a string and an integer
# print('The Result is ' + (int(x) + int(y)))  # TypeError
# print('The Result is ' + (int(x + y)))       # TypeError


print('The Result is ' + str(int(x + y)))       # 711 | string konkatenation
#
# ablauf
# x + y → '7' + '11' = '711' (String-Konkatenation), da standartwerte strings sind!
# int('711') → 711 umgewandlung vom string zum int
# str(711) → '711' umgewandlung vom int zum string
# 'The Result is ' + '711' → 'The Result is 711' (String)

print('The Result is ' + str(int(x) + int(y)))  # 18 | 7 + 11 == 18 dann vom int zum string umgewandelt
#
# ablauf
# int(x) → 7    (Integer) explizite typumwandlung vom string '7'  zum int 7
# int(y) → 11   (Integer) explizite typumwandlung vom string '11' zum int 11
# 7 + 11 → 18   (Integer) adition der int werte
# str(18) → '18' umgewandlung vom int zum string
# 'The Result is ' + '18' → 'The Result is 18' (String)
