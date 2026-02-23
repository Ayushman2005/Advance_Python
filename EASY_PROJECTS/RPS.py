import random

choices = ["rock", "paper", "scissor"]
user_score = 0
computer_score = 0
rounds = 3

for r in range(1, rounds + 1):
    print(f"\nRound {r}")
    user_choice = input("Enter rock, paper, or scissor: ")

    if user_choice != choices:
        print("Invalid choice. Round skipped.")
        continue

    computer_choice = random.choice(choices)

    print("You:", user_choice)
    print("Computer:", computer_choice)

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

print("\nFinal Score:")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("You won the game!")
elif user_score < computer_score:
    print("Computer won the game!")
else:
    print("Game tied!")
