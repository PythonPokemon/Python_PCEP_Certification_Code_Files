"""
lesen und schreiben von variablen 
"""
#---------------------------------------------------------------------------------
# lesen einer globalen variable innerhalb einer funktion:
value1 = 23         # globale variable


def my_function1():
    print(value1)   # die funktion liest die globale variable


my_function1()      # 23 |lesen geht!
#---------------------------------------------------------------------------------
# Überschreiben einer globale variable durch eine funktion :
value2 = 42


def my_function2():
    value2 = 67     # Versuch den wert einer globale variable zu überschreiben 
                    # die lokale variable 'value2' ist ausgegraut weil sie
                    # nicht benutzt wird
    #print(value2)  # kommentiere das links aus, um value2 zu testen!

my_function2()
print(value2)       # 42 | überschreiben geht nicht!
#---------------------------------------------------------------------------------
# 'Richtiges' Überschreiben einer globale variable durch eine funktion :
value3 = 74


def my_function3():
    global value3   # sagst du dem Interpreter innerhalb der Funktion explizit, 
                    # dass du auf die bereits existierende globale Variable value3 
                    # zugreifen und sie verändern möchtest.
    value3 = 99


my_function3()
print(value3)  # 99
#---------------------------------------------------------------------------------