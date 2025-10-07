age_input = input()
age_count = 0
total_age = 0
average_age = 0
# TODO: Your code here
while age_input != "done":
    age_count += 1
    total_age += int(age_input)
    age_input = input()

if age_count >= 1 and age_count <= 120:
    average_age = total_age / age_count
else:
    print(0)

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
