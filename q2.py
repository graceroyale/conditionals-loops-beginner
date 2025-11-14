# This is a guessing game. The user has to guess a predefined number until they are correct.
secret_number = 11
guess = None
while guess != secret_number:
    try: 
        guess = int(input("Guess the secret number: "))
        if guess < secret_number:
            print("Too low! Try again. Better luck next time.")
        elif guess > secret_number:
            print("Too high! Try again. Better luck next time.")
        else:
            print("Congratulations! You've guessed the correct number.")
    except ValueError:
        print("You need to enter a number! Try again. Better luck next time.")
