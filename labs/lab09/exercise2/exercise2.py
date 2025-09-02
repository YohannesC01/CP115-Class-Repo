employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if tax_status == "single" and base_salary >= 5000:
    tax_rate = 22
else:
    tax_rate = 18

if tax_status == "married" and base_salary >= 6000:
    tax_rate = 20
else:
    tax_rate =  15

if tax_status == "head" and base_salary >= 5500:
    tax_rate = 25
else:
    tax_rate = 19

EPF = 11/100
SOCSO = 0.05/100
net_salary = ((tax_rate + EPF + SOCSO) * base_salary)  + (35 * overtime_hours)



print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")