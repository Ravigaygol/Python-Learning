# Rock, Paper, Scissors

#rock = 1
#paper = 2
#scissors = 3

# 1 beats 3
# 1 loses 2

# 2 beats 1
# 2 loses 3

# 3 beats 2
# 3 loses 1

import random

def rock_paper_scissors():
    player_one = random.randint(1, 3)
    player_two = random.randint(1, 3)
    
    if player_one == 1:
        if player_two == 1:
            print('rock DRAWNS rock')
        elif player_two == 2:
            print('rock LOSES paper')
        else:
            print('rock BEATS scissors')
    elif player_one == 2:
        if player_one == 1:
            print('paper BEATS rock')
        elif player_one == 2:
            print('paper DRAWNS paper')
        else:
            print('paper LOSES scissors')
    else:
        if player_two == 1:
            print('scissors LOSES rock')
        elif player_two == 2:
            print('scissors BEATS paper')
        else:
            print('scissors DRAWN scissors')                                        


rock_paper_scissors()