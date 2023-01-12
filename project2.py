from random import randint

t = ["Rock", "Paper", "Scissors"]
score1 = 0
score2 = 0
state1 = ''
state2 = ''


computer = t[randint(0,2)]

player = False

#def RPS(lose):
# player = input("Rock, Paper, Scissors?")
#       print (computer)
#       if player == computer:
#           print("draw")
#       elif player == "Rock":
#           if computer == "Paper":
#              print("You lose!")


#def RPS(win):

#def RPS(draw):



while player == False:

    player = input("Rock, Paper, Scissors?")
    print (computer)
    if player == computer:
        print("draw")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!")
            state1 = 'win'
            state2 = 'lose'
        else:
            print("You win!")
            state1 = 'lose'
            state2 = 'win'
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!")
            state1 = 'win'
            state2 = 'lose'
        else:
            print("You win!")
            state1 = 'lose'
            state2 = 'win'
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose")
            state1 = 'win'
            state2 = 'lose'
        else:
            print("You win")
            state1 = 'lose'
            state2 = 'win'
    else:
        print("Not valid")
    if player == "x":
        print (score1 , score2)
        exit()
    else:
        player = False
        computer = t[randint(0,2)]
    if state1 == 'win':
        score1 += 1
    elif state2 == 'win':
        score2 += 1

    if score1 > score2:
        print("lose")
    elif score2 > score1:
        print("win")
    elif score1 == score2:
        print("draw")



