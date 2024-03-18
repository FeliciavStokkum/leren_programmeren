import random

score = 0
rounds = 0

while rounds < 20:
    secret_number = random.randint(1, 1000)
    print(f"The secret number is: {secret_number}")

    guesses_left = 10
    while guesses_left > 0:
        guess = 0
        while guess == 0:
            guess = input(f"Guess a number between 1 and 1000 (type 'quit' to quit): ")

            if guess == "quit":
                print(f"Your final score is: {score}")
                exit()
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                guess = 0

        if guess == 0:
            break
        if guess < 1 or guess > 1000:
            print("Invalid range. Please enter a number between 1 and 1000.")
            continue

        difference = abs(guess - secret_number)

        guesses_left -= 1
        if difference <= 50 and difference > 20:
            print(f"Warm!")
            print()
        if difference <= 20:
            print(f"Very warm!")
            print()
        if guess < secret_number:
            print(f"Too low. Try again. You have {guesses_left} guesses left.")
            print()
        elif guess > secret_number:
            print(f"Too high. Try again. You have {guesses_left} guesses left.")
            print()
        else:
            print(f"Congratulations! You guessed the number in {20 - guesses_left} guesses!")
            score += 1
            break

    print(f"Your score after round {rounds + 1} is: {score}")

    if rounds < 19:
        print("Do you want to play another round? (yes/no) ")

        while True:
            question = input(": ").lower()
            if question in ['yes', 'no']:
                break
            else:
                print("Please answer 'yes' or 'no'.")
        if question == 'no':
            break

    rounds += 1

print(f"Your final score is: {score}")