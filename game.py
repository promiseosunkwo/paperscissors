import random 



def play():
    my_input = input(f'What is yor choice? [s] for scissors, [r] for rock and [p] for paper! ')
    computer_choice = random.choice(['p','s','r'])

    if my_input == computer_choice:
        return "it's a tie"

    if is_win(my_input, computer_choice):
        return "You won!"

    return "You Lost!"  

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and player == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())