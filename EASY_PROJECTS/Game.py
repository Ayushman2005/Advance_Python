import random
print("Simple Dice Game")
n = int(input("Enter number of players: "))
players = [input(f"Enter name of player {i+1}: ") for i in range(n)]
while True:
    scores = {}
    print("\nRolling dice 5 times...\n")
    for p in players:
        total = 0
        for i in range(5):
            total += random.randint(1, 6)
        scores[p] = total
        print(p, "score:", total)
    max_score = max(scores.values())
    winners = [p for p in scores if scores[p] == max_score]
    if len(winners) == 1:
        print("\nWinner is:", winners[0])
    else:
        print("\nIt's a tie between:", ", ".join(winners))
    if input("\nPlay another round? (yes/no): ").lower() != "yes":
        print("Game Over")
        break