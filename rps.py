#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:30:11 2018

@author: eugene
"""

# rps.py

import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def random_play():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human+computer in 'rockpaperscissorsrock':
        return 'computer'
    else:
        return 'human'
    
    
    
def main(input = input):
    human = ''
    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')
        
        
    computer = random_play()
    print(computer)
    
    
    result = determine_game_result(human, computer)
    if result == 'tie':
        print('tie')
    else:
        print (result, 'wins')



if __name__ == '__main__':
    main()





# =============================================================================
# human = input('rock, paper or scissors? ')
# 
# while human not in ['rock', 'paper', 'scissors']:
#     human = input('rock, paper or scissors? ')
# 
# computer = random.choice(['rock', 'paper', 'scissors'])
# 
# print(computer)
# 
# if human == computer:
#     print('it\'s a tie!')
# elif human == 'rock' and computer == 'scissors':
#     print ('Human win')
# elif human == 'rock' and computer == 'paper':
#     print ('Computer win')
# elif human == 'scissors' and computer == 'rock':
#     print ('Computer win')
# elif human == 'scissors' and computer == 'paper':
#     print ('Human win')
# elif human == 'paper' and computer == 'rock':
#     print ('Human win')
# elif human == 'paper' and computer == 'scissors':
#     print ('Computerpaper win')     
#     ...  # tuhle část jistě zvládnete napsat sami
#     
# =============================================================================
    
    