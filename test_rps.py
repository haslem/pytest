#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:58:52 2018

@author: eugene
"""
import rps
import pytest
import subprocess
import sys


def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True
    
    
def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True


def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True



def test_lizard_is_not_valid_play():
    assert rps.is_valid_play('lizard') is False  
    
    
def test_spock_is_not_valid_play():
    assert rps.is_valid_play('spock') is False



def test_random_play_is_valid():
    for _ in range(100):
        play = rps.random_play()
        assert rps.is_valid_play(play)
        
        
        
def test_random_play_is_fairish():
    plays = [rps.random_play() for _ in range(1000)]
    assert plays.count('rock') > 100
    assert plays.count('paper') > 100
    assert plays.count('scissors') > 100
    
    
    
    
def test_paper_beats_rock():
    assert rps.determine_game_result('paper', 'rock') == 'human'
    
    
def test_paper_losses_scissors():
    assert rps.determine_game_result('paper', 'scissors') == 'computer'    
    

def test_paper_tie_paper():
    assert rps.determine_game_result('paper', 'paper') == 'tie'



def input_fake(fake):
    def input_fake_(prompt):
        print(prompt)
        return fake
    return input_fake_



# =============================================================================
# def input_fake_rock(prompt):
#     print (prompt)
#     return 'rock'
# =============================================================================
    

#monkeypatch replace one function by another
@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])    
def test_whole_game(capsys, play):
    #monkeypatch.setattr('builtins.input', input_fake_rock)
    rps.main(input = input_fake(play))
    out, err = capsys.readouterr()
    assert 'rock, paper or scissors?' in out
    assert (('computer wins' in out) or ('human wins' in out) or
    ('tie' in out))



# =============================================================================
# def test_game_asks_again_if_wrong_input():
#     cp = subprocess.run([sys.executable, 'rps.py'],
#                         input = 'asdf\nrock',
#                         encoding = 'utf-8',
#                         stdout = subprocess.PIPE)
#     assert cp.stdout.count('rock, paper or scissors?') == 2
# =============================================================================
    
    
def run_app(input):
    cp = subprocess.run([sys.executable, 'rps.py'],
                        input = 'asdf\nrock',
                        encoding = 'utf-8',
                        stdout = subprocess.PIPE)
    return cp.stdout
    
        

def test_game_asks_again_if_wrong_input():
    assert run_app('adsf\nrock').count('rock, paper or scissors?') == 2
        
    
        