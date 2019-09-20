# Current work so far. We are able to play 10,000 games of 1 hand. 
# This function does not play the contest to completion, 
# just the first hand of the competition over and over. 
# In addition we cannot see the tiebreaker function's result.
# Working on a way to use a print() to show the tiebreaker is actually working behind the scenes. 
# A poor man's debug if you will.

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:59:58 2019

@author: 16303
"""

import random
import time

start_time=time.time()
game_list=[]
# make a game a dictionary, not an array so you can store key vals in it
# the better bet is to make it a class, but this will do it quick n' dirrty
game={}

game_round=0
def pk_result():
    # name your variables more carefully
    playerOneCards=list(range(1,11))
    playerTwoCards=list(range(1,11))
    a=random.choice(playerOneCards)
    b=random.choice(playerTwoCards)
    print('PlayerA is using {}.'.format(a))
    print('PlayerB is using {}.'.format(b))

    if a == b:
        options=['front','back']
        coin=random.choice(options)
               
        # Gotta love this fake ass coin.
        if coin == "front":
            print('PlayerA wins coin flip')
            game["winner"] = "PlayerA"
            playerOneCards.append(a)
            playerTwoCards.remove(a)

        elif coin == "back":
            print('PlayerB wins coin flip')
            game["winner"] = "PlayerB"
            playerOneCards.remove(b)
            playerTwoCards.append(b)
    
    # PlayerA wins!
    elif a > b:
        print('PlayerA wins')
        game["winner"] = "PlayerA"
        playerOneCards.append(b)
        playerTwoCards.remove(b)
            
    # PlayerB wins!
    elif a < b:
        print('PlayberB wins')
        game["winner"] = "PlayerB"
        playerOneCards.remove(a)
        playerTwoCards.append(a)
    print(playerOneCards)
    print(playerTwoCards)

    # logic missing to play the round to completion
    # something like check if either playerA or playerB has zero cards before declaring a winner.
    # that should be a game() function which calls hand() until the end game case breaks out.

for i in range(10): # make 10K later
    pk_result()
    game["round"] = i + 1
    # even can do game time if you want
    # Bug where PlayerB always wins?
    game_list.append(game)
    print("The number of rounds is:",i)
    
end_time=time.time()
print(game_list)
print("Time takes {}.".format(end_time-start_time)) 


