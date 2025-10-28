# TODO: Your code here
for number in range(100):
    if number % 7 == 0:
        found_number = 91
        break 
    print(f'Number divisible by 7: {number}')

    if number % 13 == 0:
        found_number = 91
        break  
    print(f'Number divisible by 13: {number}')

print(found_number)
