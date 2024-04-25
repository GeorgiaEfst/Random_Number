import random

def set_limits():
    while True:
        lower_limit = int(input("Give lower limit: "))
        upper_limit = int(input("Give higher limit: "))
        max_attempts = int(input("Please enter the attempt limit: "))
        if lower_limit < upper_limit:
            return lower_limit, upper_limit, max_attempts
        else:
            print("The lower limit has to be smaller that the higher limit.")

def get_guess(lower_limit, upper_limit):
    guess = int(input(f"Give number between {lower_limit} and {upper_limit}: "))
    return guess

def check_guess(guess, secret_number):
    if guess < secret_number:
        print("The number is less than the requested.Please try again.")
    elif guess > secret_number:
        print("The number is bigger than the requested.Please try again.")
    else:
        print("Congrats!!You guess the mystery number.")

def play_game():
    lower_limit, upper_limit, max_attempts = set_limits()
    secret_number = random.randint(lower_limit, upper_limit)
    attempts = 0

    while attempts < max_attempts:
        guess = get_guess(lower_limit, upper_limit)
        attempts += 1
        if guess == secret_number:
            print(f"You tried {attempts} times.")
            break
        else:
            check_guess(guess, secret_number)
    else:
        print(f"Unfortunately the number of attempts has run out...The secret number is: {secret_number}. Good luck next time :)")

if __name__ == "__main__":
    print("Welcome to the secret number guessing game. Good luck!")
    play_game()