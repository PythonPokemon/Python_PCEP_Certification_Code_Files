"""
zum nachlesen
...
"""
print("Python funktioniert!")

# krasser stuff
def beispiel(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)


beispiel(1, 2, 7, 8, 9, farbe="rot, gelb", zahl=3.14, y=15)
#--------------------------------------------------------------------------------------------------------
""""
| Index | Wert |
| :---- | :--- |
| 0     | 3    |
| 1     | 1    |
| 2     | -2   |
| -1    | -2   |
| -2    | 1    |
| -3    | 3    |

"""

my_list = [ 3, 1,-2]

print(my_list[my_list[-1]]) 
#--------------------------------------------------------------------------------------------------------
# function ohne parameter, aber mit variablen außerhalb der function
argument_var_name = "Jakob"
argument_var_Geburtsjahr = 1990, 10, 7

def function():
    print("hallo ich heiße: ", argument_var_name, "mein geburtsjahr ist: ", argument_var_Geburtsjahr)

function()

#--------------------------------------------------------------------------------------------------------
# function mit integrierten variablen als parameter, die variablen liegen außerhalb der function
# da die variablen als paramter/argument übernommen wurde, erwartet die function mindestens genauso viel paramter
# beim functions aufruf
argument_var_name1 = "Jakob"
argument_var_Geburtsjahr1 = 1990, 10, 7

def function(argument_var_name1, argument_var_Geburtsjahr1):
    print("hallo ich heiße: ", argument_var_name1, "mein geburtsjahr ist: ", argument_var_Geburtsjahr1)

function(argument_var_name1, argument_var_Geburtsjahr1)

# shadowing / überschattung von variablen
param1 = 123456789
param2 = "aaaaaaaaaaaa"
param3 = 0.123

def message(param1, param2, param3):
    # variablen die innerhalb einer methode als parameter verwendet werden
    # werden mit den werten innerhalb der methode überschattet/verdeckt!
    param1 = 1223334444
    param2 = 3.14159265359
    param3 = "string"
    print("ein text und 3 params == ", param1, param2, param3)

message(1, 3.14, "string")
message(123, 456, 789)
message(1.1, 2.22, 3.333)
message("a", "bb", "ccc")


print(param1)
print(param2)
print(param3)
#--------------------------------------------------------------------------------------------------------
# shadowing / überschattung von variablen gegenbeispiel
print("\n gegenbeispiel-shadowing\n")
param1 = 123456789
param2 = "aaaaaaaaaaaa"
param3 = 0.123

def message(param1, param2, param3):
    print("ein text und 3 params == ", param1, param2, param3)

message(1, 3.14, "string")
message(123, 456, 789)
message(1.1, 2.22, 3.333)
message("a", "bb", "ccc")


print(param1)
print(param2)
print(param3)
#--------------------------------------------------------------------------------------------------------
def instrucktion(a, b=2, *args, **kwargs):
    print("positionalargument: ", a, "Default:", b, "beliebig viele args:", args, "beliebig viele kwargs:",  kwargs)

instrucktion(1, 3, 4, 4, x=10, y=200)
instrucktion(1.234, 0.99, 0.1, 0.2, x=0.987654321, y=999999999.999999999)
instrucktion('a', 'b', 'auch wörter als nur 1 arg', 'viele', 'viele argumente', xyz='keyargs')
instrucktion("aaaaa", "bbbbb", "ganz viele argumente", "noch mehr argumente", abcdefghijklmnopqrstuvwxyz=123456789, z=0.0001)
instrucktion(0.1, 9, 'abcdefg', "hijklmnop", qrstuvwxyz=0.1, gent=122333444455555666666777777788888888999999999)
#--------------------------------------------------------------------------------------------------------
import webbrowser  # Modul zum Öffnen von Webseiten

def strange_function(n):
    if n % 2 == 0:  # Prüft, ob n ohne Rest durch 2 teilbar ist
        print("Modulo 0 erkannt – starte Musik 🎵")
        webbrowser.open("https://youtu.be/3VxqVNCJDA0?si=rqjQ2gh7-mrcH8t8")
        return True

# Beispielaufrufe
strange_function(4)  # Öffnet YouTube
strange_function(5)  # Gibt nur Text aus

#--------------------------------------------------------------------------------------------------------
def strange_function_none(n):
    if n % 2 == 0:  # Prüft, ob n ohne Rest durch 2 teilbar ist
        return True
    
print(strange_function_none(2))
print(strange_function_none(1))
#--------------------------------------------------------------------------------------------------------

def my_list(n):
    list = []
    for i in range(0,n):
        list.insert(0,i)
    return list
    
print(my_list(5))

x= my_list
print(x)    # gibt die speicheradresse aus!

#--------------------------------------------------------------------------------------------------------
# global var
def my_function():
    global var
    var = 2
    print("zugriff und manipulation in der methode auf globale variable: ", var)

var = 1
print("bevor die globale variable in der methode ein neuer wert zugewiesen wurde:", var)

my_function()
print(var)
#--------------------------------------------------------------------------------------------------------
# Namederror variable innerhalb der methode, nicht global
def my_function():
    var = 2
    print("zugriff und manipulation in der methode auf globale variable: ", var)

my_function()
print(var)
#--------------------------------------------------------------------------------------------------------
# tupel und variablen
tuple = (1,)
var_tuple = (1)

print(tuple)
print(var_tuple)
#--------------------------------------------------------------------------------------------------------
list = [1,2,3,4]
print(list)

tuple = (1,2,3,4)
print(tuple)
#--------------------------------------------------------------------------------------------------------
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

# standart abfrage
for i in dictionary.keys():
    print("Zeige den schlüssel:-->", i, "<---und den wert:--->", dictionary[i])

# mit der .items() methode, als schlüsselwertpaar und verpackten tupels
print("----------------------------------------------------------------------")
for i in dictionary.items():
    print(i)

# mit der .items() methode, als schlüsselwertpaar und entspackten tupels
print("----------------------------------------------------------------------")
for schlüssel, wert in dictionary.items():
    print("einzelne ausgaben der schlüssel:--->", schlüssel, "<---und werte:--->", wert)

"""
das ist equivalenz dazu:
paar = ("x", "y")
a, b = paar  # Entpacken

print(a)  # x
print(b)  # y
"""

# mit der .values() methode gibt man nur werte aus, keine schlüssel!
print("----------------------------------------------------------------------")
for i in dictionary.values():
    print("ausgabe der werte:", i)
#--------------------------------------------------------------------------------------------------------
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

# modifiezieren von werten
print(dictionary["ape"])    # vor der modfizierung!
dictionary["ape"] = "Monkey.D.Luffy"
print(dictionary["ape"])    # nach der modifizierung!

# hinzufügen neuer paare: key:value
print(dictionary)           # davor!
dictionary["Pirate King"] = "Gold.D.Roger" #  key[] = value
print(dictionary)           # danach

# oder hinzufügen über .update() methode
dictionary.update({"Hokage":"Naruto"})
print(dictionary)

# removing keys | löscht auch automatisch die werte
del dictionary["Hokage"]
print(dictionary)

#--------------------------------------------------------------------------------------------------------
# dictionarys
dictionary = {"cat":"katze", "dog":"hund", "ape":"affe"}

print(dictionary) # bevor das letzte paar entfernt wird!
dictionary.popitem()
print(dictionary)   # nachdem entfern des letzten key:value pair
#--------------------------------------------------------------------------------------------------------
# and = 2   #keyword
true = 1
TRUE = 3
# True = 4  #keyword
FALSE = 5
false = 6
# False = 7 #keyword


print(true)
# print(and)
print(TRUE)
# print(True)
print(FALSE)
print(false)
# Print(False)
#--------------------------------------------------------------------------------------------------------

# Ganzzahl division == ZoroDivisionError
x = int(input("gib eine zahl ein: "))
y = int(input("gi die zweite zahl ein: "))

x = x // y
y = y // x

print(y)
#--------------------------------------------------------------------------------------------------------
# list comprehansion entweder so
my_list = [0 for i in range(1, 3)]

print(my_list)
#-------------------------------------------
# oder list comprehansion mit variablen namen 
# als ausdruck
# dieser typ wird dann übernommen
variable = "abc"

my_list2 = [variable for i in range(1, 3)]

print(my_list2)

#--------------------------------------------------------------------------------------------------------

# else wird immer ausgeführt hier
for i in range(1):
    print("#")
else:
    print("#")

#--------------------------------------------------------------------------------------------------------
# 2 Dimensionale list comprehension:
"""
| i | 3 - i |
| - | ----- |
| 0 | 3     |
| 1 | 2     |
| 2 | 1     |
--------------------------------------------------
diagonale aufsummieren!
[index 2D:   0  1  2
        0   [3, 2, 1],
        1   [3, 2, 1],
        2   [3, 2, 1]
]
--------------------------------------------------
Wir nehmen immer das Element auf Position [i][i].

➤ i = 0

t[0][0] = 3
s = 3

➤ i = 1

t[1][1] = 2
s = 3 + 2 = 5

➤ i = 2

t[2][2] = 1
s = 5 + 1 = 6
--------------------------------------------------
"""

t = [[3-i for i in range(3)] for j in range(3)]
s = 0

for i in range(3):
    s += t[i][i]
print(s)

#--------------------------------------------------------------------------------------------------------
vals = [0, 1, 2]    # 3 elements
vals.insert(0, 1)   # add 1 element

print(vals)         # 4 elements
del vals[1] # löscht den wert auf index 1
print(vals)

#--------------------------------------------------------------------------------------------------------
# keyword 'in' that's why Syntaxerror
# try insteat with 'it'

# def fun(in=2, out=3):
#     return in * out

# print(fun(3))
#--------------------------------------------------------------------------------------------------------

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return
    
print(fun(fun(2)) +1)   # +1 erzeugt TypeError
#--------------------------------------------------------------------------------------------------------
def fun(inp=2, out=3):
    return inp * out

print(fun(out=2))   # man darf 1x kwargs stehen lassen, aber nicht kwars, pos
#--------------------------------------------------------------------------------------------------------
def f(x):
    if x == 0:
        return 0
    return x + f (x -1)

print(f(3))

"""
f(3) == 6
f(2) == 3
f(1) == 1
"""
#--------------------------------------------------------------------------------------------------------

my_list = ['Mary', 'had', 'a', 'little', 'lamb']


def my_list(my_list):
    del my_list[3]
    my_list[3] = 'ram'

print(my_list(my_list)) # try it so: print(my_list)

"""
1️⃣ Problem: Name-Kollision

Du hast zwei Dinge mit demselben Namen my_list:

my_list ist zuerst eine Liste, Danach definierst du my_list als Funktion
Python überschreibt dann die Liste durch die Funktion. 
Ab dem Moment der Funktionsdefinition ist my_list nicht mehr die Liste, 
sondern die Funktion.
"""
#--------------------------------------------------------------------------------------------------------
foo = (1, 2, 3)

foo.index(1) # output 1
foo.index(0) # valueError

# foo.index[0] TypeError
#--------------------------------------------------------------------------------------------------------

# gibt die werte des dictionarys als variablen aus
# bestimmt mit [0] den key-Index
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")
#--------------------------------------------------------------------------------------------------------
x = 3
y = 2

x = x % y
x = x % y
y = y & x
print(y)
#--------------------------------------------------------------------------------------------------------
my_list = [ x * x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(my_list))
#--------------------------------------------------------------------------------------------------------
"""
✅ Summe der Fehler: 5 Fehler

break außerhalb einer Schleife → SyntaxError
except: vor spezifischem except block → SyntaxError
Unerreichbarer except Block → SyntaxError
Code hinter print(5/0) wird nie ausgeführt → logischer Fehler
ZeroDivisionError wird nicht spezifisch behandelt → logischer Fehler
"""

# try:
#     print(5/0)
#     break
# except:
#     print("Sorry, something went wrong")
# except (ValueError, ZeroDivisionError):
#     print("Too bad...")

#--------------------------------------------------------------------------------------------------------

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1,my_list[v])

print(my_list)
#--------------------------------------------------------------------------------------------------------

"""
📘 Beispiel mit deinen Fehlern

Du willst abfangen:

TypeError
ValueError
ZeroDivisionError
AttributeError
"""

try:
    # Code, der Fehler machen kann
    print(19/0)
except (TypeError, ValueError, ZeroDivisionError, AttributeError):
    print("Einer dieser Fehler ist passiert.")

"""
🧠 Warum funktionieren runde Klammern so?

Ein Anfänger-Bild:

Die Klammern sind wie eine Box voller erlaubter Fehler.
Wenn einer dieser Fehler passiert → springt Python in den except-Block.
"""
#--------------------------------------------------------------------------------------------------------
# die variable 'ch' soll nicht 'in' hi nach charakert suchen...
# sondern das ist nur eine irreführung!
# iat normale for i in range()
for ch in "hi":
    print(ch)

#--------------------------------------------------------------------------------------------------------
x = 1
y = 1.0
z = "1"

if x == y:
    print("one")

if y == int(z):
    print("two")

# elif wird nur ausgeführt wenn das if darüber nicht true ist!
elif x == y:     
    print("three")

# else/sonst wird nur ausgeführt wenn alles davor false war!
else:
    print("four")

#--------------------------------------------------------------------------------------------------------
# kommentar
try:
    value = input("Enter a value: ")
    print(value/value)
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
#--------------------------------------------------------------------------------------------------------
# ✅ ❌

try:
    print(5 + "3")
except TypeError:
    print("❌ zahlen sind mit strings nicht addierbar")
#-------------------------------------------------------------------------------------------
try:
    zahleingabe = int(input("Gib eine zahl ein:"))
    summe = 10 + zahleingabe
    print("die zahl ist: ", summe)
except ValueError:
    print("❌ der typ war korrekt aber falscher wert!, es wurde eine --->Zahl<--- erwartet")
#-------------------------------------------------------------------------------------------
try:
    print(6//0)
except ZeroDivisionError:
    print("❌ eine division durch 0 ist nicht möglich!")
#-------------------------------------------------------------------------------------------
try:
    list = [1, 2, 3]
    print(list[3])
except IndexError:
    print("❌ der aufgerufene index existiert nicht!")
#-------------------------------------------------------------------------------------------
try:
    tuple = (1, 2, 3)
    tuple.append(4)
except AttributeError:
    print("❌ Tupel sind immutable/unveränderlich und besitzen deshalb diese methode nicht!")
#-------------------------------------------------------------------------------------------
try:
    dictionary = {"a":1, "b":2}
    print(dictionary["c"])
except KeyError:
    print("❌ der key ist nicht vorhanden")
#-------------------------------------------------------------------------------------------
try:
    #var = 1
    print(var)
except NameError:
    print("❌ die variable die aufgerufen wird, existiert nicht!")
#-------------------------------------------------------------------------------------------
try:
    #print("hallo)
    print("probier mal den print mit einem anführungszeichen, darüber!")
except SyntaxError:
    print("❌ Syntaxfehler können nicht abgefangen werden!")
#-------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
