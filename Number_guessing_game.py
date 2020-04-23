print("SlackUsername - BlackAdam")
print("Welcome User")
print("There are three levels in this game \n Easy \n Medium \n Hard")


###########################
def input_number(message):
    while True:
        try:
            userinput = int(input(message))
        except ValueError:
            print("Not a number, enter a number")
            continue
        else:
            return userinput
            break

### Easy level parameters
Guess_trial_easy_level = 0
Guess_limit_easy_level = 6

##### Medium level parameters
Guess_trial_medium_level = 0
Guess_limit_medium_level = 4


###### Hard Level Parameters
Guess_trial_hard_level = 0
Guess_limit_hard_level = 3

### Correct guess for each level
Easy_correct_guess = 6
Medium_correct_guess = 14
Hard_correct_guess = 25

#######
status = True

while status:
 ####################

    Level = input("Enter the level you will love to play: ").lower()

#### Easy stage
    if  Level == "easy" :
        print("Welcome to Easy Level \n You have 6 trials")
        print("The number is between 1 - 10")
        while Guess_trial_easy_level < Guess_limit_easy_level :
            User_easy_level_guess = input_number("Enter Guess Number: ")
            Guess_trial_easy_level += 1
            if User_easy_level_guess == Easy_correct_guess:
                print("You got it right")
                print("Game terminated")
                break
            else:
                print("You are wrong")
                print("You have used " + str(Guess_trial_easy_level) + " of your 6 trials")


    ### Medium Stage
    elif Level == "medium" :
        print("Welcome to Medium Level \n You have 4 trials")
        print("The number is between 1 - 20")
        while Guess_trial_medium_level < Guess_limit_medium_level :
            User_medium_level_guess = input_number("Enter Guess Number: ")
            Guess_trial_medium_level += 1
            if User_medium_level_guess == Medium_correct_guess:
                print("You got it right")
                print("Game terminated")
                break
            else:
                print("You are wrong")
                print("You have used " + str(Guess_trial_medium_level) + " of your 4 trials")



    ### Hard stage
    elif Level == "hard" :
        print("Welcome to Hard Level \n You have 3 trials")
        print("The number is between 1 - 50")
        while Guess_trial_hard_level < Guess_limit_hard_level :
            User_hard_level_guess = input_number("Enter Guess Number: ")
            Guess_trial_hard_level += 1
            if User_hard_level_guess == Hard_correct_guess:
                print("You got it right")
                print("Game terminated")
                break
            else:
                print("You are wrong")
                print("You have used " + str(Guess_trial_hard_level) + " of your 3 trials")




    else:
        print("wrong input")
        print("There are three levels in this game \n Easy \n Medium \n Hard")
    Play_again = input("Would you like to play again: Enter YES or NO: ").lower()
    if Play_again == "no":
        status = False
        print("Thank you for playing the game")

    else:
        status = True



