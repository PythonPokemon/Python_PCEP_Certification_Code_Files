
from sys import argv
sum = 0
for i in range(2, len(argv)):
    sum += float(argv[i])
print(

    "The average score for {0} is {1:.2f}"

    .format(argv[1], sum/(len(argv)-2))
)
