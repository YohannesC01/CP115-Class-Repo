totalgrade = 0
valid_count = 0

for i in range(100):
    grade = float(input())
    if grade < 0:
        break
    totalgrade += grade
    valid_count += 1


average = totalgrade / valid_count

print(valid_count)
print(f"{average:.2f}")

