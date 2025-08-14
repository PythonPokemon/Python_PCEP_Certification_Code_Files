
data = {'one': 'two', 'two': 'three', 'three': 'one'}
res = data['three']

for _ in range(len(data)):
    res = data[res]

print(res)  # one
