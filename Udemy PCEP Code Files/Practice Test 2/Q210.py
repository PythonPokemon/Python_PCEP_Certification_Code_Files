
i = 0
while i < i + 2:
    i += 1
    print('*')
    if i == 1000:
        print("1000 erreicht!")
        break  # Safeguard
else:
    print('*')
