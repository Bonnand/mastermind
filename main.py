import random
import os

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
    list=true_combinaison
    list2=user_combinaison

    for idx in range(len(user_combinaison)):
        if(user_combinaison[idx]==true_combinaison[idx]):
                list[idx]="_"
                list2[idx]="#"

    for first_idx in range(len(list)):
        for second_idx in range(len(list2)):

            if(list[first_idx]==list2[second_idx]):
                number+=1

    return number

'''test the number of correct colors in user's combinaison'''
def number_correct_colors(user_combinaison,true_combinaison):

    number_correct=0

    for idx in range(len(user_combinaison)):
        if(user_combinaison[idx]==true_combinaison[idx]):
            number_correct+=1

    return number_correct

def test_file(file_path):

    if (os.path.isfile(file_path) == 1):
        return True
    else:
        return False

def write_file(file_path,value):

        with open(file_path, 'w') as file:
            file.write(value)


def read_file(file_path):
    with open(file_path, 'r') as file:
        lignes = file.readlines()

        return lignes[0]

def statistics_display(games_played,score):
    print("Number of games_played : " + str(games_played))
    print("Score : " + str(score))


def game():
    replay = True
    try_max=12
    code_lenght=4


    if(test_file(".statistics/games_played.txt")==False):
        write_file(".statistics/games_played.txt","0")

    if (test_file(".statistics/score.txt") == False):
        write_file(".statistics/score.txt","0")

    games_played=int(read_file('.statistics/games_played.txt'))
    score=int(read_file('.statistics/score.txt'))


    print("code lenght : " + str(code_lenght))
    statistics_display(games_played,score)


    print("Standard colors : Red|Green|Blue|Yellow|Purple|White")
    choice=input("Do you want to choose your colors or standart colors ? (your/standard)")

    if(choice=="your"):
        color_choosed = choose_color()
    elif(choice=="standard"):
        color_choosed = [[0], ["R", "G", "B", "Y", "P", "W"]]


    true_combinaison=["R","G","B","Y"]


    while(replay):

        choice = input("What do you want to do : play/replay or leave or reset")

        if(choice=="play" or choice=="replay"):
            game_over=False
            try_number = 0
            '''true_combinaison = random_combinaison(color_choosed[1], code_lenght)'''

            while(try_number!=try_max and game_over==False):

                print(true_combinaison)

                user_combinaison = ask_combinaison()
                number_of_correct_colors=number_correct_colors(user_combinaison,true_combinaison)
                number_of_partial_colors=number_partial_colors(user_combinaison,true_combinaison)


                if(number_of_correct_colors==4):
                    game_over=True
                else:
                    print("Correct : " + str(number_of_correct_colors) +" | Partial : "+ str(number_of_partial_colors))
                    print("Try again !")
                try_number += 1


            if(game_over):
                print("You win with "+str(try_number)+" attemps")
                print("12 - "+str(try_number))
                score+=1

            else:
                print("You lose sorry :( ")

            games_played+=1
            statistics_display(games_played,score)
            write_file(".statistics/games_played.txt", str(games_played))
            write_file(".statistics/score.txt", str(score))

        elif (choice == "leave"):
            print("You leave the game")
            replay= False

        elif (choice == "reset"):
            games_played=0
            score=0
            write_file(".statistics/games_played.txt","0")
            write_file(".statistics/score.txt", "0")
            statistics_display(games_played, score)


    print("Game finish")

game()