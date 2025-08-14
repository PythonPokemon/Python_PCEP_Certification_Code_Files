
i = 4
while i > 0:    # i ist 4
    i -= 2      # i ist 2
    print('*')  # *
    if i == 2:  # Yip, i ist 2
        break   # verlasse die Schleife
else:           # der rest wird nicht ausgeführt, wenn die Schleife verlassen wird!
    print('*')
