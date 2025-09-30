num_days = int(input())
danger_threshold = float(input())
danger_days = 0
total_temperatures = 0
# TODO: Your code here
# Use input() inside the loop to get each day's temperature
for days_num in range(num_days):
    temperatures = float(input())
    total_temperatures += temperatures

    if temperatures > danger_threshold:
        danger_days += 1
    

average_temp = total_temperatures / num_days

print(danger_days)
print(f"{average_temp:.1f}")