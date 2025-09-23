position = input()
overtime_hours = int(input())
is_weekend = input()
hourly_rate = 0

# TODO: Your code here
if position == "Manager":
    hourly_rate = 35
elif position == "Supervisor":
    hourly_rate = 25
elif position == "Staff":
    hourly_rate = 18
else: 
    hourly_rate = 0


overtime_pay = (hourly_rate * overtime_hours) * 1.5

if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5

total_pay = overtime_pay

print(hourly_rate)
print(overtime_pay)
print(total_pay)
