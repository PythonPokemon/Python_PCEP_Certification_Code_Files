
nums = [1, 2, 3]
vals = nums
del vals[:] #löschfunktion
print(nums)  # []
print(vals)  # []

# Referenztest == Speicheradresse ist Identisch, deshalb wird bei deiden der löschvorgang ausgeführt!
print(id(nums)) # 2805438898368
print(id(vals)) # 2805438898368