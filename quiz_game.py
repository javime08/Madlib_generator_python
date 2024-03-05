import time
print('Welcome to the quiz game!')
playing = input('Do you want to play y/n ')
if playing != 'yes':
    quit()
print('GOOD, lets play then!')
start_time = time.time()

questions = {
    'question1':{
        'question': 'Final “Mario Kart” course? ',
        'answer':'rainbow road'
    },
    'question2':{
        'question': 'Mario’s origin game?',
        'answer':'donkey kong'
    },
    'question3':{
        'question': 'Solids Snake franchise?',
        'answer':'Metal gear'
    },
    'question4':{
        'question': 'v-bucks currency in?',
        'answer':'fortnite'
    },
    'question5':{
        'question': 'nintendos initial products?',
        'answer':'playing cards'
    },
    'question6':{
        'question': 'pearls color in splatoon 2?',
        'answer':'pink'
    },
    'question7':{
        'question': 'astro boys type?',
        'answer':'platformer'
    },
    'question8':{
        'question': 'first nintendo optical disk console',
        'answer':'gamecube'
    },
    'question9':{
        'question': 'Cuphead overworlds count?',
        'answer':'three'
    },
    'question10':{
        'question': 'Jack mitchells friend in "Call of duty: advanced warfare?"',
        'answer':'Gideon'
    },
    'question11':{
        'question': 'First character in "injustice 2?"',
        'answer':'Batman'
    },
    'question12':{
        'question': 'Best-selling game in october 2017?',
        'answer':'playerunknown battlegrounds'
    },
    'question13':{
        'question': 'Cover star of "Madden nfl 18?"',
        'answer':'Tom Brady'
    },
    'question14':{
        'question': '"Zelda" princess name? .',
        'answer':'Zelda'
    },
    'question15':{
        'question': '"Overwatch" healer?',
        'answer':'mercy'
    },
    'question16':{
        'question': 'Pokemon most famous electric type?',
        'answer':'pikachu'
    },
    'question17':{
        'question': 'Sonics nemesis',
        'answer':'Dr. Robotnik'
    },
    'question18':{
        'question': 'Street fighter fireball move?',
        'answer':'hadouken'
    },
    'question18':{
        'question': 'tetris shape name?',
        'answer':'teroniminoes'
    },
    'question19':{
        'question': 'resident evil virus?',
        'answer':'t-virus'
    },
    'question20':{
        'question': 'super mario nemesis',
        'answer':'Bowser'
    },
}
score = 0
for key, value in questions.items():
    print(value['question'])
    answer = input('Answer?: ')

    if answer.lower() == value['answer'.lower()]:
        print('correct!')
        score +=1
        print('score: '+str(score))
    else:
        print('HAHA you suck!')
        print('Correct answer: ' + value['answer'])
        print('score: '+str(score))

print('Your score is: '+str(score) + 'of 20 questions')
end_time = time.time()
total_time = end_time - start_time
print('GOOD JOB, your time was: ',total_time,' seconds!!')