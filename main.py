import random
import os
from tkinter import *
from tkinter import ttk

'''Correct colors : number of good color and good placement'''
'''Partial colors : number of good color but bad placement'''

'''Colors definition       (Useless)

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
'''
def choose_color():
    color=["None"]*6
    initial=["None"]*6

    print("Write 6 color with her initial")
    for idx in range(6):
        color[idx]=input("Write color "+str(idx+1))
        initial[idx]=input("Write initial")

    return [color,initial]

'''Ask the user to obtain a potential true combination'''
def ask_combination(code_lenght):
    combination = input("Write combination with "+str(code_lenght)+" colors (example : R-G-B-Y for RED GREEN BLUE YELLOW)")
    combination = combination.split("-")

    return(combination)


'''Creation of random code with user's colors '''
def random_combination(color_choosed,code_lenght):
    random_list=["None"]*code_lenght

    for idx in range(code_lenght):
        random_list[idx]=random.choice(color_choosed)

    return random_list

'''test the number of partial colors in user's combination'''
def number_partial_colors(user_combination, true_combination):

    number=0
    true_combination_copy=true_combination.copy()
    user_combination_copy=user_combination.copy()

    for idx in range(len(user_combination)):
        if(user_combination[idx]==true_combination[idx]):
                true_combination_copy[idx]="_"
                user_combination_copy[idx]="#"

    for first_idx in range(len(true_combination_copy)):
        for second_idx in range(len(user_combination_copy)):

            if(true_combination_copy[first_idx]==user_combination_copy[second_idx]):
                true_combination_copy[first_idx]="-"
                user_combination_copy[second_idx]="#"
                number+=1

    return number

'''test the number of correct colors in user's combination'''
def number_correct_colors(user_combination, true_combination):

    number_correct=0

    for idx in range(len(user_combination)):
        if(user_combination[idx]==true_combination[idx]):
            number_correct+=1

    return number_correct

'''Test if the file name : "file_path" exist'''
def test_file(file_path):

    if (os.path.isfile(file_path) == 1):
        return True
    else:
        return False

'''permet to write a value in a file'''
def write_file(file_path,value):

        with open(file_path, 'w') as file:
            file.write(value)
            file.close()

'''permet to read a value in a file'''
def read_file(file_path):
    with open(file_path, 'r') as file:
        lignes = file.readlines()
        file.close()

        return lignes[0]

'''It's saying in fonction's name '''
def statistics_display(games_played,score):
    print("Number of games_played : " + str(games_played))
    print("Score : " + str(score))


def game():
    '''Definition of variables'''

    replay = True
    try_max=12
    code_lenght=4
    first_play=True
    validated_colors=False
    validated_combination=False

    '''Create and write a "0" if file doesn't exist'''

    if(test_file(".statistics/games_played.txt")==False):
        write_file(".statistics/games_played.txt","0")

    if (test_file(".statistics/score.txt") == False):
        write_file(".statistics/score.txt","0")

    '''Read statistics of those two files'''

    games_played=int(read_file('.statistics/games_played.txt'))
    score=int(read_file('.statistics/score.txt'))


    print("code lenght : " + str(code_lenght))
    statistics_display(games_played,score)


    print("Standard colors : Red|Green|Blue|Yellow|Purple|White")

    while(validated_colors==False):
        choice=input("Do you want to choose your colors or standard colors ? (your/standard)")

        if(choice=="your"):
            color_choosed = choose_color()
            validated_colors=True

        elif(choice=="standard"):
            color_choosed = [[0], ["R", "G", "B", "Y", "P", "W"]]
            validated_colors=True

        if(validated_colors==False):
            print("Please answer to the question")

    #true_combination=["W","W","R"]


    while(replay):

        if(first_play):
            choice = input("What do you want to do : play/leave/reset")
        else:
            choice = input("What do you want to do : replay/leave/reset")

        if(choice=="play" or choice=="replay"):

            '''Variables initialisation/reinitialisation'''

            first_play=False
            game_over=False
            try_number = 0
            true_combination = random_combination(color_choosed[1], code_lenght)

            while(try_number!=try_max and game_over==False):

                #print(true_combination)

                while(validated_combination==False):

                    user_combination = ask_combination(code_lenght)

                    '''if user don't write a good code, code asking him again'''
                    if(len(user_combination)==code_lenght):
                        validated_combination=True
                    else:
                        print("You don't write a good combination, try again !")

                validated_combination=False

                number_of_correct_colors=number_correct_colors(user_combination,true_combination)
                number_of_partial_colors=number_partial_colors(user_combination,true_combination)


                if(number_of_correct_colors==len(true_combination)):
                    game_over=True
                else:
                    print("Correct : " + str(number_of_correct_colors) +" | Partial : "+ str(number_of_partial_colors))
                    print("Try again !")
                try_number += 1


            if(game_over):
                print(f"You win with {str(try_number)} attempt{'s' if try_number>1 else ''}")
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

'''game()'''

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
