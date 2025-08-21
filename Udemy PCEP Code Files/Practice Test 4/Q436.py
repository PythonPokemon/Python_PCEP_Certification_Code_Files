


order, state = int('1700'), 'FL'  # in order wird der wert 1700 gespeichert | in state 'FL'
delivery = 0


if state in ['NC', 'SC', 'VA']:
    if order <= 1000:
        delivery = 70
    elif 1000 < order < 2000:
        delivery = 80
    else:
        delivery = 90
else:
    delivery = 50                       # +50
    print('1. delivery', delivery)      
if state in ['GA', 'WV', 'FL']:         # FL enthalten
    if order > 1000:                    # ja order 1700 ist größer 1000
        delivery += 30                  # +30
        print('2. delivery', delivery)  
    if order < 2000 and state in ['WV', 'FL']:  # UND bedingung! | wenn 1.700 kleiner 2.000 ist UND 'FL' enthalten
        delivery += 40                  # +40
        print('3. delivery', delivery)  
    else:
        delivery += 25
print(delivery)                         # 120 | 50 + 30 + 40 == 120
