


'''Colors definition'''

R="Red"
G="Green"
B="Blue"
Y="Yellow"
P="Purple"
W="White"

'''Ask the user to obtain a potential true combinaison'''
def ask_combinaison():
    combinaison = input("Write combinaison : first second third four")
    combinaison = combinaison.split()
    print(combinaison)
    '''first_color = combinaison[0]
    second_color = combinaison[1]
    third_color = combinaison[2]
    fourth_color = combinaison[3]
    return(first_color+second_color+third_color+fourth_color)'''
    return(combinaison)

'''test if the user combinaison is the same that the true combinaison'''
def partial_number_color(user_combinaison,true_combinaison):

    partial_number=0;

    for first_idx in range(len(user_combinaison)):
        for second_idx in range(len(true_combinaison)):
            if(user_combinaison[first_idx]==true_combinaison[second_idx] and user_combinaison[second_idx]!=true_combinaison[second_idx]):
                partial_number+=1

    return partial_number


user_combinaison=ask_combinaison()
true_combinaison=['G','R','B','P']
print(partial_number_color(user_combinaison,true_combinaison))
