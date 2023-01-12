import random
choices = ['sang', 'kaghaz', 'gheichi']
state1 = ''
state2 = input()
states = [('sang', 'kaghaz', 'lost', 'win'),
             ('sang', 'gheichi', 'win', 'lost'),
              ('kaghaz', 'gheichi', 'lost', 'win'),]
choice1 = choices.random()
choice2 = state2
scorex = 0
scorey = 0
 if choice1 not in choices and choice2 not in choices:
     state1 = 'draw'
     state2 = 'draw'
 elif choice1 not in choices:
     state1 = 'win'
     state2 = 'lost'
 elif choice2 not in choices:
     state1 = 'lost'
     state2 = 'win'
 else:
     if choice1 == choice2:
     state1 = 'draw'
     state2 = 'draw'
           else:
               for s in states:
                   if choice1 == s[0] and choice2 == s[1]:
                       state1 = s[2]
                       state2 = s[3]
                   elif choice1 == s[1] and choice2 == s[0]:
                       state1 = s[3]
                       state2 = s[2] 
if state1 == 'win':
    score1 += 1
    print("win")
 elif state2 == 'win':
    score2 += 1
    print("lose")
else:
    print('draw')
