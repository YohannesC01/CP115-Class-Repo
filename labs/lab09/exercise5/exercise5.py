main_course = input()
drink = input()
dessert = input()
customer_age = int(input())

# TODO: Your code here\
main_course_prices = {"Chicken": 10, "Beef": 12, "Fish": 11}
drink_prices = {"Soft Drink": 2, "Coffee": 3}
dessert_prices = {"Ice Cream": 4, "Cake": 5}

food_cost = 0
if main_course in main_course_prices:
    food_cost += main_course_prices[main_course]
if drink in drink_prices:
    food_cost += drink_prices[drink]
if dessert in dessert_prices:
    food_cost += dessert_prices[dessert]

total_with_service = food_cost * 1.10

if customer_age > 60:
    final_bill = total_with_service * 0.85  # 15% off
elif customer_age < 18:
    final_bill = total_with_service * 0.90  # 10% off
else:
    final_bill = total_with_service

print(f"{final_bill:.2f}")



print(f"{final_bill:.2f}")