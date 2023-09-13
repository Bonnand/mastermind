import random

'''Correct colors : number of good color and good placement'''
'''Partial colors : number of good color but bad placement'''

'''Colors definition'''

def recognize_color(color):
    if(color=="R"):
        return "Red"
    elif (color == "G"):
        return "Green"
    elif (color == "B"):
        return "Blue"
    elif (color == "Y"):
        return "Yellow"
    elif (color == "P"):
        return "Purple"
    elif (color == "W"):
        return "White"

def choose_color():
    color=["None"]*6
    initial=["None"]*6

    print("Write 6 color with her initial")
    for idx in range(6):
        color[idx]=input("Write color "+str(idx+1))
        initial[idx]=input("Write initial")

    return [color,initial]

'''Ask the user to obtain a potential true combinaison'''
def ask_combinaison():
    combinaison = input("Write combinaison : first second third four")
    combinaison = combinaison.split()

    return(combinaison)

def random_combinaison(color_choosed,code_lenght):
    random_list=["None"]*code_lenght

    for idx in range(code_lenght):
        random_list[idx]=random.choice(color_choosed)

    return random_list

'''test the number of partial colors in user's combinaison'''
def number_partial_colors(user_combinaison,true_combinaison):

    number=0
    list=user_combinaison

    for idx in range(len(user_combinaison)):
        for idx2 in range(len(user_combinaison)):
            if(user_combinaison[idx]==true_combinaison[idx2]):
                list[idx]="_"

    for first_idx in range(len(user_combinaison)):
        for second_idx in range(len(true_combinaison)):

            if(user_combinaison[first_idx]==true_combinaison[second_idx]):
                number+=1

    return number

'''test the number of correct colors in user's combinaison'''
def number_correct_colors(user_combinaison,true_combinaison):

    number_correct=0

    for idx in range(len(user_combinaison)):
        if(user_combinaison[idx]==true_combinaison[idx]):
            number_correct+=1

    return number_correct



def game():
    try_number=0
    try_max=12
    code_lenght=4
    win=False
    replay=True

    '''color_choosed=choose_color()'''
    color_choosed=[[0],["R","G","B","Y","P","W"]]
    print("code lenght : "+ str(code_lenght))
    true_combinaison = random_combinaison(color_choosed[1],code_lenght)
    '''true_combinaison=["G","R","B","Y"]'''


    while(replay):

        while(try_number!=try_max and win==False):

            print(true_combinaison)

            user_combinaison = ask_combinaison()
            number_of_correct_colors=number_correct_colors(user_combinaison,true_combinaison)
            number_of_partial_colors=number_partial_colors(user_combinaison,true_combinaison)

            if(number_of_correct_colors==4):
                win=True
            else:
                print("Number of partial colors : " + str(number_of_partial_colors))
                print("Number of correct colors : " + str(number_of_correct_colors))
                print("Try again !")
            try_number += 1


        if(win):
            print("You win with "+str(try_number)+" attemps")
        else:
            print("You lose sorry :( ")

        choice=input("Do you want replay ?")
        if(choice=="no"):
            replay=False
        else:
            try_number=0
            win=False
            true_combinaison = random_combinaison(color_choosed[1], code_lenght)

    print("Game over")


game()