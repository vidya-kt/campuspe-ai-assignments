import random

best_score = 100   # large value for comparison

play_again = "yes"

while play_again == "yes":

    number = random.randint(1, 100)
    attempts = 7
    used = 0
    guessed = False

    print("\nI have selected a number between 1 and 100")
    print("You have 7 attempts to guess it")

    while attempts > 0:

        guess = int(input("Enter your guess: "))
        used = used + 1
        attempts = attempts - 1

        if guess == number:
            print("Congratulations! You guessed the number")
            print("Attempts used:", used)
            guessed = True

            if used < best_score:
                best_score = used
                print("New best score:", best_score)

            break

        elif guess > number:
            print("Too high")

        else:
            print("Too low")

        # hint when close (within 5)
        if guess != number:
            if guess > number:
                diff = guess - number
            else:
                diff = number - guess

            if diff <= 5:
                print("Hint: You are very close!")

        print("Attempts remaining:", attempts)

    if guessed == False:
        print("You failed to guess the number")
        print("The number was:", number)

    play_again = input("Do you want to play again? (yes/no): ")

print("Best score in this session:", best_score)
print("Game over")