import random

Playing = True

while Playing:

    # Get range limit from user input
    stop_range = input("Enter range limit: ")

    # Validate input
    if not stop_range.isdigit() or int(stop_range) <= 0:
        print("Please enter a number greater than 0.")
        quit()

    stop_range = int(stop_range)

    # Generate a random number within the given range
    random_number = random.randint(0, stop_range)
    guess_score = 0

    # Start the guessing game loop
    while True:
        guess_score += 1
        user_guess = input("Make a guess: ")

        if not user_guess.isdigit() or int(user_guess) <= 0:
            print("Please re-enter a number greater than 0.")
            continue

        user_guess = int(user_guess)

        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")

    print(f"You got it in {guess_score} attempts.")

    choice = input("DO you want to play again (yes/no): ").lower()

    if choice != "yes":
        Playing = False
