employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
if tax_status == "single" and base_salary >= 5000:
    tax_rate = 0.22

elif tax_status == "married" and base_salary <= 5000:
    tax_rate = 0.18

if tax_status == "married" and base_salary >= 6000:
    tax_rate = 0.20

elif tax_status == "single" and base_salary <= 6000:
    tax_rate =  0.15

if tax_status == "head" and base_salary >= 5500:
    tax_rate = 0.25

elif tax_status == "head" and base_salary <= 5500:
    tax_rate = 0.19

EPF = 11/100
SOCSO = 5/100
net_salary = ((tax_rate + EPF + SOCSO) * base_salary)  + (35 * overtime_hours)



print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")