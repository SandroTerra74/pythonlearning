import random
generatedNumber = random.randrange(1,10)
userGuess = int(input('Guess a number in the range 1-10:'))
if userGuess==generatedNumber:
    print("You've got it right!")
elif userGuess<generatedNumber:
    print('Your guess is too low!')
else:
    print('Your guess is too high!')