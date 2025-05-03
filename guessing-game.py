import random
import time

start_time = time.time()

while True:
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100")
    guess = int(input())

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You win!")

    if guess != number:
        print(f"Wrong! The number was {number}")

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break

print(f"Time taken: {time.time() - start_time:.2f}s")
