# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)

    if len(opponent_history) > 2:
        last_three = opponent_history[-3:]
        last_two = opponent_history[-2:]

        if last_two.count(last_two[0]) == 2:  # Opponent repeated the same move twice
            guess = 'S' if last_two[0] == 'P' else 'P' if last_two[0] == 'R' else 'R'
        elif len(last_three) >= 2 and last_three[-2] == last_two[0] and last_three[-2] != last_three[-1]:  # Opponent changed their move after a repetition
            guess = 'S' if last_three[-2] == 'P' else 'P' if last_three[-2] == 'R' else 'R'
        elif last_two[0] == last_two[1]:  # Opponent repeated the same move twice
            guess = 'S' if last_two[0] == 'P' else 'P' if last_two[0] == 'R' else 'R'
        elif last_two[0] == 'P' and last_two[1] == 'R':  # Opponent played Paper then Rock
            guess = 'S'
        elif last_two[0] == 'R' and last_two[1] == 'S':  # Opponent played Rock then Scissors
            guess = 'P'
        elif last_two[0] == 'S' and last_two[1] == 'P':  # Opponent played Scissors then Paper
            guess = 'R'
        elif prev_opponent_play == '':
            guess = random.choice(['R', 'P', 'S'])
        elif prev_opponent_play == 'R' and opponent_history[-2] == 'R':
            guess = 'S'
        elif prev_opponent_play == 'P' and opponent_history[-2] == 'P':
            guess = 'R'
        elif prev_opponent_play == 'S' and opponent_history[-2] == 'S':
            guess = 'P'
        elif prev_opponent_play == 'R' and opponent_history[-2] == 'S':
            guess = 'P'
        elif prev_opponent_play == 'P' and opponent_history[-2] == 'R':
            guess = 'S'
        elif prev_opponent_play == 'S' and opponent_history[-2] == 'R':
            guess = 'P'
        elif prev_opponent_play == 'R' and opponent_history[-2] == 'P':
            guess = 'S'
        elif prev_opponent_play == 'P' and opponent_history[-2] == 'S':
            guess = 'R'
        elif prev_opponent_play == 'S' and opponent_history[-2] == 'P':
            guess = 'R'
        elif prev_opponent_play == 'R' and opponent_history[-2] == 'R' and opponent_history[-3] == 'R':
            guess = 'P'
        elif prev_opponent_play == 'R' and opponent_history[-2] == 'R' and opponent_history[-3] == 'P':
            guess = 'S'
        else:
            guess = random.choice(['R', 'P', 'S'])
    else:
        guess = random.choice(['R', 'P', 'S'])

    return guess