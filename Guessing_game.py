# generate a num from 1 to 10
from random import randint
answer = randint(1,10)
while True:

    try:
       guess = int(input('Enter a num 1-10:  '))
       if guess>0 and guess<11:
           if guess==answer:
               print('You are a genius')
               break
           else:
               print('Try again ')
       else:
           print('I said a num between 1-10')

    except ValueError:
        print('Plz enter a num ')
        continue
        
