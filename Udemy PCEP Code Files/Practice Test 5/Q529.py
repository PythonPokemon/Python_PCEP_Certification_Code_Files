
data = [1, 2, [3, 4], [5, 6], 7, [8, 9]]
count = 0

for i in range(len(data)):
    if type(data[i]) == list:
        count += 1

print(count)  # 3
