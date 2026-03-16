import random

number = random.randint(1, 100)
guess = 0
num_guesses = 0

print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have the following chances to guess the correct number.\n""")

print("""Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")

choice = int(input("Enter your choice: "))
print()

if (choice == 1):
    print("""Great! You have selected the Easy difficulty level.
Let's start the game!\n""")
    while (num_guesses < 10):
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if (guess == number):
            print("Congratulations! You guessed the correct number in {} attempts.".format(num_guesses))
            break
        elif (guess > number):
            print("Incorrect! The number is less than {}.\n".format(guess))
        elif (guess < number):
            print("Incorrect! The number is greater than {}.\n".format(guess))
    if (num_guesses == 10):
        print("You took 10 incorrect attempts. The correct number is {}.".format(num_guesses, number))
elif (choice == 2):
    print("""Great! You have selected the Medium difficulty level.
Let's start the game!\n""")
    while (num_guesses < 5):
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if (guess == number):
            print("Congratulations! You guessed the correct number in {} attempts.".format(num_guesses))
            break
        elif (guess > number):
            print("Incorrect! The number is less than {}.\n".format(guess))
        elif (guess < number):
            print("Incorrect! The number is greater than {}.\n".format(guess))
    if (num_guesses == 5):
        print("You took 5 incorrect attempts. The correct number is {}.".format(num_guesses, number))
elif (choice == 3):
    print("""Great! You have selected the Hard difficulty level.
Let's start the game!\n""")
    while (num_guesses < 3):
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if (guess == number):
            print("Congratulations! You guessed the correct number in {} attempts.".format(num_guesses))
            break
        elif (guess > number):
            print("Incorrect! The number is less than {}.\n".format(guess))
        elif (guess < number):
            print("Incorrect! The number is greater than {}.\n".format(guess))
    if (num_guesses == 3):
        print("You took 3 incorrect attempts. The correct number is {}.".format(num_guesses, number))
else:
    print("Invalid choice. Try again.")