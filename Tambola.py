import random
def generate_ticket():
    return sorted(random.sample(range(1, 91), 15))
def display_ticket(name, ticket, marked):
    print(f"\n{name}'s Ticket:")
    for num in ticket:
        if num in marked:
            print(f"[{num:2d}]", end=" ")
        else:
            print(f" {num:2d} ", end=" ")
    print()
def tambola_game():
    while True:
        players = int(input("Enter number of players (1-9): "))
        if 1 <= players <= 9:
            break
        print("Players must be between 1 and 9")
    player_data = {}
    for i in range(players):
        name = input(f"Enter name of player {i+1}: ")
        player_data[name] = {
            "ticket": generate_ticket(),
            "marked": set()
        }
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    print("\n Tambola Game Started ")
    for num in numbers:
        input("\nPress Enter to pick next number...")
        print(f"\n Number called: {num}")
        for name, data in player_data.items():
            if num in data["ticket"]:
                data["marked"].add(num)
            display_ticket(name, data["ticket"], data["marked"])
            if len(data["marked"]) == 15:
                print(f"\n {name} WINS! FULL HOUSE")
                return
while True:
    tambola_game()
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "no" or choice == "No":
        print("\nThank you for playing Tambola ")
        break