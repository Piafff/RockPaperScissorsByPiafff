import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

player_move = input('Chose [r]ock, [p]aper or [s]cissors: ')


if player_move == 'r':
    player_move = rock
elif player_move == 'p':
    player_move = paper
elif player_move == 's':
    player_move = scissors
else:
    print('Invalid input. Try again...')
    exit()

computer_random_choice = random.randint(1, 3)
computer_move = ''

if computer_random_choice == 1:
    computer_move = rock
elif computer_random_choice == 2:
    computer_move = paper
elif computer_random_choice == 3:
    computer_move = scissors

print(f'The computer chose {computer_move}')

if (player_move == rock and computer_move == rock) or (player_move == paper and computer_move == paper) or \
        (player_move == scissors and computer_move == scissors):
    print('Draw!')
elif (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print('You win!')
else:
    print('You lose!')