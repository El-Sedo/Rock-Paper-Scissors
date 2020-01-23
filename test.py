import random

print("Welcome\n")

def rules():    #These are the rules of the game
    print("In Rock-Paper-Scissors, you have three options which are Rock, Paper and Scissors (as the name implies).")
    print("Your opponent also has to pick from one of the three options.")
    print("Rock always beats Scissors, Scissors Cuts Paper, and Paper Blows Rock.\n So choose wisely.\n")
    print("Good Luck")



# Let's give the computer a choice
def comp():
    global comp_choice
    compans = random.randint(1,3)
    if compans == 1:
        comp_choice = 'Rock'
    elif compans == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"

# PLayer decides
def player():
    global play_choice,rockn
    rockn = input(str("1. Rock \n2. Paper \n3. Scissors\n")) #we are convertinig to string so we can perform .upper
    rockn = rockn.upper()
    if (rockn == '1') | (rockn == 'R') | (rockn == 'ROCK'):
        play_choice = 'Rock'
    elif (rockn == '2')| (rockn == 'P') | (rockn == 'PAPER'):
        play_choice = 'Paper'
    elif (rockn == '3')| (rockn == 'S') | (rockn == 'SCISSORS'):
        play_choice = 'Scissors'
    else:
        print('wrong input, please try again')
        return player()

# Now we need to decide who wins the game
def score():
    winc = 0
    winp = 0
    if (play_choice == 'Rock'):
        if (comp_choice == 'Rock'):
            print('DRAW\n')
        elif (comp_choice == 'Paper'):
            print('COMPUTER WINS\n')
            winc += 1
        else:
            print('YOU WIN\n')
            winp += 1
    elif (play_choice == 'Paper'):
        if (comp_choice == 'Rock'):
            print('YOU WIN')
            winp += 1
        elif(comp_choice == 'Paper'):
            print('DRAW')
        else:
            print('COMPUTER WINS')
            winc += 1
    elif (play_choice == 'Scissors'):
        if (comp_choice == 'Rock'):
            print('COMPUTER WINS')
            winc += 1
        elif(comp_choice == 'Paper'):
            print('YOU WIN')
            winp += 1
        elif(comp_choice == 'SCissors'):
            print('DRAW')
    print('\n')
    print("Player: {} \t Computer: {}".format(winp,winc))


def game(): #This is the game proper
    player()    #we call the player's choice
    print("\n")
    print('YOU \t vs \t COMPUTER')
    comp()      # we call the computer's choice
    print(play_choice, " \t vs \t ", comp_choice, "\n")
    score()






# We let the user decide if he wants to see the instructions first
r1 = input("Do you want instructions? \n Yes or No: ")  #for those wwho doon't know how to play the gamw
r1 = r1.upper()  #we account for case sensitivity
if (r1 =='Y'):
    rules()
    print("\nOkay\n")
    game()
else:
    print("\nOkay\n")
 #   for i in range(5):
        game()




