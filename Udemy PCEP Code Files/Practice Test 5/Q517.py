"""
x startwert 0
x iteriert durch die liste 'nums' solange x kleiner 10 ist
anschließend wird der wert in x zwischengespechert und ausgegeben
wenn x dem wert 7 entspricht soll abgebrochen werden
sonst soll der wert in x um 1 erhöht werden
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
while x < 10:         # 
    print(nums[x])    # 
    if nums[x] == 7:  # 
        break         
    else:             
        x += 1        
