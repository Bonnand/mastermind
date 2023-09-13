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


'''Ask the user to obtain a potential true combinaison'''
def ask_combinaison():
    combinaison = input("Write combinaison : first second third four")
    combinaison = combinaison.split()

    return(combinaison)

def random_combinaison():
    random_list=["None"]*4
    random_colors_list=["R","G","B","Y","P","W"]

    for idx in range(4):
        random_list[idx]=random.choice(random_colors_list)

    return random_list

'''test the number of partial colors in user's combinaison'''
def number_partial_colors(user_combinaison,true_combinaison,number_correct):

    number=0

    for first_idx in range(len(user_combinaison)):
        for second_idx in range(len(true_combinaison)):
            if(user_combinaison[first_idx]==true_combinaison[second_idx] and '''
            
                    user_combinaison[second_idx]==true_combinaison[second_idx]'''):
                number+=1

    number_partial=(number-number_correct)

    return number_partial

'''test the number of correct colors in user's combinaison'''
def number_correct_colors(user_combinaison,true_combinaison):

    number_correct=0

    for idx in range(len(user_combinaison)):
        if(user_combinaison[idx]==true_combinaison[idx]):
            number_correct+=1

    return number_correct



def game():
    try_number=0
    win=False
    true_combinaison = random_combinaison()
    print(true_combinaison)

    while(try_number!=12 and win==False):

        user_combinaison = ask_combinaison()
        number_of_correct_colors=number_correct_colors(user_combinaison,true_combinaison)
        number_of_partial_colors=number_partial_colors(user_combinaison,true_combinaison,
                                            number_correct_colors(user_combinaison,true_combinaison) )

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

game()