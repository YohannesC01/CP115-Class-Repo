main_dish = 25
dish_amount = 3
appetizers = 12
appetizers_amount = 2
drinks = 8
drink_amount = 4
service_tax = 0.10
delivery_fee= 5

total_bill = (main_dish * dish_amount)+(appetizers * appetizers_amount)+(drinks * drink_amount)+ delivery_fee
tax = (service_tax*total_bill)
bill_pay = total_bill + tax
split_bill = bill_pay //6

print(f"{split_bill}")