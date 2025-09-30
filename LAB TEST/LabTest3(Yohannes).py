usage = int(input("Total Usage:"))

#determine how much the discount they get
if usage <= 50 :
    discount = 0
elif usage >= 50 or usage <= 100:
    discount = 0.05
elif usage >= 100:
    discount = 0.20

#calculate total bill paid
TotalBill_paid = usage - (discount * usage)

print(TotalBill_paid)