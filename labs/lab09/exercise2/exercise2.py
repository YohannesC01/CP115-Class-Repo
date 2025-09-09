employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

tax_rate = 0.0

# TODO your code here
if tax_status == "Single" and base_salary >= 5000:
    tax_rate = 0.22

elif tax_status == "Single" and base_salary <= 5000:
    tax_rate = 0.18

elif tax_status == "Married" and base_salary >= 6000:
    tax_rate = 0.20

elif tax_status == "Married" and base_salary <= 6000:
    tax_rate =  0.15

elif tax_status == "Head" and base_salary >= 5500:
    tax_rate = 0.25

elif tax_status == "Head" and base_salary <= 5500:
    tax_rate = 0.19

overtime_pay = 35 * overtime_hours
totalincome = base_salary + overtime_pay
after_tax = totalincome * (1 - tax_rate)
net_salary = after_tax * (1 - 0.115)
tax_rate_str = f"{int(tax_rate * 100)}%"




print(employee_name)
print(tax_rate_str)
print(f"{net_salary:.2f}")