
str1 = 'Peter'
str2 = str1[:]       # unnötig!
# str2 = str1        # liste aus str1 wird str2 zugewiesen!

print(id(str1))  # e.g. 140539652049216
print(id(str2))  # e.g. 140539652049216 (da der inhalt exact gleich ist, verweisen beide aufs gleiche) == speicher sparen!
print(str1 is str2)  # True
print(str1 == str2)  # True

print(str1)
print(str2)

