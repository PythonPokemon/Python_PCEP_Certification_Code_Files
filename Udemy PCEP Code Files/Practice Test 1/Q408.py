"""
Frage 27
Übersprungen
Q408

What is the expected output of the following code?



box = {}
jars = {}
crates = {}
 
box['biscuit'] = 1
box['cake'] = 3
 
jars['jam'] = 4
 
crates['box'] = box
crates['jars'] = jars
 
print(len(crates[box]))
---------------------------------------------------
Richtige Antwort
The code is erroneous.

"""

box = {}                    # erzeugung Dictionary {}
jars = {}                   # erzeugung Dictionary {}
crates = {}                 # erzeugung Dictionary {}

box['biscuit'] = 1          # wertzuweisung im Dictionary: key 'biscuit' :  wert 1 | die sich in der Referenzvariable box befindet == {'biscuit': 1,}
box['cake'] = 3             # wertzuweisung im Dictionary: key 'cake'    :  wert 3 | die sich in der Referenzvariable box befindet == {'biscuit': 1, 'cake': 3}
jars['jam'] = 4             # wertzuweisung im Dictionary: key 'jam'     :  wert 4 | die sich in der Referenzvariable jars befindet == {'jars': {'jam': 4}
crates['box'] = box         # ACHTUNG | hier wird jetzt in der variable crates, dem key 'box' : die variable box mit allen daten die darin gespeichert wurden zugewiesen == {'box': {'biscuit': 1, 'cake': 3}}
crates['jars'] = jars       # {'box': {'biscuit': 1, 'cake': 3}, 'jars': {'jam': 4}
crates ['neu'] = 100

# print(len(crates[box]))   # TypeError: unhashable type: 'dict'    | Am Ende fehlen nur noch einfache Anführungszeichen '' in der letzten Zeile ['box']
print(len(crates['box']))   # zählt die anzahl der inhalte die einem key zugeordnet sind
print(crates['neu'])        # zeigt nur die Inhalte die einem key zugeorndet sind {'biscuit': 1, 'cake': 3}
print(crates)               # zeigt alle gespicherten inhalte in der variable {'box': {'biscuit': 1, 'cake': 3}, 'jars': {'jam': 4}}

#Anzahl Inhalte:                 |                                 |                   |            == 3  da nur die übergeorneten key's gezählt werden!                  
print(len(crates))          # {'box': {'biscuit': 1, 'cake': 3}, 'jars': {'jam': 4}, 'neu': 100}
