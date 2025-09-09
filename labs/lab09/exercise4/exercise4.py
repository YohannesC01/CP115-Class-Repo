current_reading = int(input())
previous_reading = int(input())

# TODO: Your code here
consumption = current_reading - previous_reading


if consumption <= 20:
    water_cost = consumption * 0.57
elif consumption <= 35:
    water_cost = (20 * 0.57) + ((consumption - 20) * 1.03)
else:
    water_cost = (20 * 0.57) + (15 * 1.03) + ((consumption - 35) * 1.40)


service_charge = 8
sewerage = 2


total_bill = water_cost + service_charge + sewerage


print(consumption)
print(water_cost)
print(total_bill)