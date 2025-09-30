num_rounds = int(input())
total_score = 0
# TODO: Your code here
# Use input() inside the loop to get each round's score  
for round_num in range(1, num_rounds + 1):
    score = int(input())

    if score > 100:
        score += score * 0.2  

    total_score += score

final_score = total_score
rounds_processed = num_rounds

print(f"{final_score:.1f}")
print(rounds_processed)
