# guess_the_number.py

# A simple number guessing game
secret_number = 7

while True:
    x = int(input("Guess the secret number (between 1 and 10): "))
    if x == secret_number:
        print("🎉 Correct! You guessed the secret number.")
        break
    else:
        print("❌ Incorrect, try again.")
