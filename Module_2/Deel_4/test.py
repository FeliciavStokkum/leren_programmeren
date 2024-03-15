import random

score = 0
rounds = 0

while rounds < 20:
    secret_number = random.randint(1, 1000)
    print(secret_number)

    guesses = 0
    while guesses < 10:

        guess = 0
        while guess is 0:
            guess = input("Guess a number between 1 and 1000 (type 'quit' to quit): ")

            if guess == "quit":
                print(f"Your final score is: {score}")
                exit()
            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number.")
                guess = 0

        if guess is 0:
            break
        if guess < 1 or guess > 1000:
            print("Invalid range. Please enter a number between 1 and 1000.")
            continue

        difference = abs(guess - secret_number)
        guesses += 1

        if difference <= 50 and difference >20:
            print("Warm!")
        if difference <= 20:
            print("Very warm!")
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number.")
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