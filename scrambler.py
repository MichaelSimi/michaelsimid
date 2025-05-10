import random

moves = [
    "R", "L", "U", "D", "F", "B",
    "R'", "L'", "U'", "D'", "F'", "B'",
    "R2", "L2", "U2", "D2", "F2", "B2",
]


scramble_length = int(input("Enter the scramble length: "))


def scramble():
    print("Scramble:", end=" ")
    last_face = None
    for _ in range(scramble_length):
        move = random.choice(moves)
        while move[0] == last_face:  # Ensure the move doesn't start with the same face
            move = random.choice(moves)
        print(move, end=" ")
        last_face = move[0]  # Update last_face


while True:
    print_scramble = input("Press enter to scramble the cube. Type 'exit' to quit. ")
    if "exit" in print_scramble.lower() or "quit" in print_scramble.lower() or "stop" in print_scramble.lower():
        print("Exiting scramble generator.")
        break
    scramble()
    print()



