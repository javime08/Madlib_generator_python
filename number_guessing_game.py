import random
top_of_range = input('Type in a number: ')
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('dummy write down a number below 0')
        quit()

else:
    print('dummy, please type in a number')
    quit()
random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    user_guess = input('Try to guess: ')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('simpleton, type a number next time')

    if user_guess == random_number:
        print('You won!')
        guesses+=1
        print(f'number of guesses: {guesses}')
        break
    elif user_guess > random_number:
        print('Too high, keep guessing')
        guesses += 1
        print(f'number of guesses: {guesses}')
    else:
        print('Too low, keep guessing')
        guesses +=1
        print(f'number of guesses: {guesses}')
if guesses <=2:
    print('Youre good, too good....')
    print('Sus behavior')
else:
    print('Youre bad a guessing, try something else')