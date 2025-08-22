"""
'index' 0, iteriert durch 'productIdList'
solange es kleiner 10 ist, sollen die werte die 'index' in sich zwischen speichert während der iteration ausgegeben werden.
wenn 'index' den wert 6 entspricht soll abgebrochen werden
ansonsten weiter iterieren und bei jedem durchlauf den wert von 'index' +1 erhöhen
"""

productIdList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0

while index < 10:
    print(productIdList[index])   # 0 1 2 3 4 5 6
    if productIdList[index] == 6:
        break
    else:
        index += 1
