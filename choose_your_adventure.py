name = input('Whats your name?')
print(f'Welcome {name}, to this adventure!')
answer = input('You are on a dirt road, two options, left or right. Which would you choose? left or right?').lower()
if answer == 'left':
    print('You walk left, after 10 minutes of walking...')
    q2 = input('You come to a river, you can dive in and swim or you can walk across it, walk or swim? ')
    if q2 == 'swim':
        print('you try to swim, in the middle of the river there are piranhas, they eat you.')
        print('You died')
        print('RIP')
    elif q2 =='walk':
        print('you walked so much, you are tired.')
        print('you died of thirst.')
        print('RIP')
    else:
        print('Not a valid option, bye.')
elif answer == 'right':
    q3= input('You are walking in a strange path, you notice a house, with a beatiful woman, do you aproach her? yes/no')
    if q3 == 'yes':
        print('She is a vampire, she bites you')
        print('now you are a ghoul')
        print('RIP')
    elif q3 == 'no':
        print('You walk a little bit, you feel a presence')
        q4 = input('after a while you turn around and see nothing, you keep walking, there is another beatiful woman, do you talk with her? yes/no?')
        if q4 == 'yes':
            print('she is a succubus, you feel sleepy, you fall into a deep sleep')
            print('you see the woman in your dreams, she eats your soul, you died')
            print('RIP')
        elif q4 == 'no':
            print('you walk a little bit, feeling dizzy, you lay down')
            print('a snake crawls underneath you, you get bitten, you died')
            print('RIP')
        else:
            print('not a valid option')
            print('RIP')
else:
    print('Not a valid option, bye.')