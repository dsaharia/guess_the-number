# This is a guessing game.
import random

print('Hello there, What is your name ?')
name = input()

print('Hello ' + name + ', I am thinking of a number between 1 and 5')
number = random.randint(1, 5)  # random number is generated

# Ask the player for 3 guesses

for guessTaken in range(1, 4):  # guess conditions
    print('Take a guess:')
    guess = int(input())
    if guess < number:
        print('Sorry, the value is too low')
    elif guess > number:
        print('Nope, Number is too high')
    else:
        print("Great ! , That's correct")
        break

if guess == number:
    print('You took ' + str(guessTaken) + ' guesses')
    print('Have a great Day !')
if guess != number:
    print('Sorry, I was thinking of ' + str(number))
