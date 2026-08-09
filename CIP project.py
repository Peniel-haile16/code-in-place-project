import random

high_score = 0

def choose_difficulty():
    print("\nChoose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 10
        elif choice == "2":
            return 7
        elif choice == "3":
            return 5
        else:
            print("Please enter a valid choice.")

def play_game():
    global high_score

    secret_number = random.randint(1, 100)
    max_attempts = choose_difficulty()
    attempts_left = max_attempts

    print("\nI have chosen a number between 1 and 100!")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts_left > 0:
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Please choose a number between 1 and 100.")
            continue

        attempts_left -= 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            score = attempts_left + 1

            print("\n🎉 Congratulations!")
            print(f"You guessed the number {secret_number}!")

            print(f"Score: {score}")

            if score > high_score:
                high_score = score
                print("🏆 New High Score!")

            print(f"Current High Score: {high_score}")
            return

        if attempts_left > 0:
            print(f"Attempts remaining: {attempts_left}")

    print("\n💥 Game Over!")
    print(f"The number was {secret_number}.")
    print(f"Current High Score: {high_score}")

def main():
    print("=" * 40)
    print("🎮 NUMBER GUESSING GAME 🎮")
    print("=" * 40)

    while True:
        play_game()

        again = input("\nWould you like to play again? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for playing!")
            print("Goodbye!")
            break

main()
if__name__ == '__main__':
    main()
