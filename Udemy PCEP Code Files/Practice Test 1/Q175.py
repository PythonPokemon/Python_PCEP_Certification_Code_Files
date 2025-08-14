
rates = (1.2, 1.4, 1.0)
new = rates[3:]
print(new)         # ()
print(rates[-2:])  # (1.4, 1.0)

for rate in rates[-2:]:
    new += (rate,)

print(new)         # (1.4, 1.0)
print(len(new))    # 2
