"""
Frage 90
Übersprungen
Q623

The ABC company is building a basketball court for its employees to improve company morale.
You are creating a Python program that employees can use to keep track of their average score.
The program must allow users to enter their name and current scores. The program will output the user name and the user's average score.
The output must meet the following requirements:



The user name must be left-aligned If the user name has fewer than 20 characters, additional space must be added to the right The average score must at least have three places to the left of the decimal point
and one place to the right of the decimal (xxx.x)

What would you insert instead of ??? and ???
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Die ABC-Unternehmen baut einen Basketballplatz für seine Mitarbeiter, um die Moral im Unternehmen zu steigern. Sie erstellen ein Python-Programm, das die Mitarbeiter verwenden können, um ihren Durchschnittspunktestand zu verfolgen. 
Das Programm muss es den Benutzern ermöglichen, ihren Namen und ihre aktuellen Punktzahlen einzugeben. 
Das Programm gibt den Benutzernamen und den Durchschnittspunktestand des Nutzers aus. Die Ausgabe muss die folgenden Anforderungen erfüllen:

Der Benutzername muss linksbündig sein. Wenn der Benutzername weniger als 20 Zeichen hat, muss zusätzlicher Platz auf der rechten Seite hinzugefügt werden. 
Der Durchschnittswert muss mindestens drei Stellen links vom Dezimalpunkt und eine Stelle rechts vom Dezimalpunkt (xxx.x) haben.

Was würden Sie anstelle von ??? und ??? einsetzen?
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Richtige Antwort
%-20s
%5.1f
"""

name = input('What is your name?')
sum = 0
score = 0
count = 0
while score != -1:
    score = int(input('Enter your scores: (-1 to end)'))
    if score == -1:
        break
    sum += score
    count += 1
average = sum / count
print('%-20s, your average score is: %5.1f' % (name, average))
