# keyindex:--------|
#    |---0         1
data = {'1': '0', '0': '1'}

# for d in data.values():
for d in data.vals():  # AttributeError: ... | korrekt wäre .values()
    print(d, end=' ')    # gibt die werte in keyindex[0] aus == '0' und  keyindex[1] aus == '1'
