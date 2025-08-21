
marks = [80, 70, 90, 90, 80, 100]
average = sum(marks) // len(marks)
grade = ''

if 90 <= average <= 100:
    grade = 'A'
elif 80 <= average < 90:
    grade = 'B'
elif 70 <= average < 80:
    grade = 'C'
elif 65 <= average < 70:
    grade = 'D'
else:
    grade = 'F'

print(sum(marks))  # 510
print(len(marks))  # 6
print(510 // 6)    # 85
print(510 / 6)     # 85.0
print(average)     # 85 | 510 geteilt durch 6
print(grade)       # B  | da 85 zwischen 80 - 90 liegt!
