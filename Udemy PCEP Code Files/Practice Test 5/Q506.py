"""
data.keys() liefert ein dict_keys-Objekt, das nicht indexierbar ist wie eine Liste.
Deshalb funktioniert data[0] nicht - das Dictionary sucht nach dem Schlüssel 0, den es nicht gibt → KeyError.
-------------------------------------------------------------------------------------------------------------
"""

data = {'Peter': 30, 'Paul': 31}
print(list(data.keys()))    # ['Peter', 'Paul']
print(data.keys())          # dict_keys(['Peter', 'Paul'])

#print(data[0])             # keyError da kein Index