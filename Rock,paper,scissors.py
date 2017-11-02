import random
def generate_choice():
    return random.randint(1,3)

# def compare_choices(computer, user):
#
#     if user == computer:
#        return"its a tie"
#     elif user == 1 and computer == 2:
#           return"You have won"
#     elif user == 2 and computer == 3:
#            return"You have won"
#     elif user == 3 and computer == 1:
#             return"You have won"
#     else:
#       return "You have lost"
#
#
#
# def main():
#     while True:
#         computer_choice = generate_choice()
#         user_choice = int(input('Enter scissors(1), paper(2) or stone(3) :'))
#         # continue the game logic here
#         result = compare_choices(computer_choice,user_choice)
#         print("You choose %s and computer chooses %s,%s" %(user_choice,computer_choice))
#
# main()
def get_choice(number):
    if number == 1:
        return "Scissors"
    elif number == 2:
        return  "Paper"
    elif number== 3:
        return "Stone"
    else:
        return "Unknown"
def compare_choices(computer, user):
    if computer == 1:
        if user == 2:
            return "You lose"
        elif user == 3:
            return "You win"
        else:
            return "Draw"
    elif computer == 2:
        if user == 3:
            return "You lose"
        elif user == 1:
            return "You win"
        else:
            return "Draw"
    elif computer ==3:
        if user == 1:
            return "You lose"
        elif user == 2:
            return "You win"
        else:
            return "Draw"
def main():
    while True:
        computer_choice = generate_choice()
        user_choice = int(input('Enter scissors(1), paper(2) or stone(3) :'))
#         # continue the game logic here
        result = compare_choices(computer_choice,user_choice)
        print("You choose %s and computer chooses %s,%s" %(get_choice(user_choice),get_choice(computer_choice),result))
        if not result == "Draw":
            break


main()

