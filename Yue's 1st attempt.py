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

def play_a_game(round_counts, game_list):
    game={}
    hands=0

    playerOneCards=list(range(1,11))
    playerTwoCards=list(range(1,11))

    while len(playerOneCards) > 0 or len(playerTwoCards) > 0:
        # check the winner conditions
        if len(playerOneCards) == 0:
            game["winner"] = "PlayerTwo"
            game["hands_played"] = hands
            game_list.append(game)
            round_counts.append(hands)
            print('PlayerTwo won in this many hands:', hands)
            return game

        elif len(playerTwoCards) == 0:
            game["winner"] = "PlayerOne"
            game["hands_played"] = hands
            game_list.append(game)

            round_counts.append(hands)
            print('PlayerOne won in this many hands:', hands)
            return game
        else:
            # Otherwise play another hand
            play_a_hand(playerOneCards, playerTwoCards)
            hands += 1
   
def play_a_hand(playerOneCards, playerTwoCards):
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
            playerOneCards.append(a)
            playerTwoCards.remove(a)

        elif coin == "back":
            print('PlayerB wins coin flip')
            playerOneCards.remove(b)
            playerTwoCards.append(b)
    
    elif a > b:
        print('PlayerA wins the hand')
        playerOneCards.append(b)
        playerTwoCards.remove(b)
            
    elif a < b:
        print('PlayberB wins the hand')
        playerOneCards.remove(a)
        playerTwoCards.append(a)
    print(playerOneCards)
    print(playerTwoCards)

for i in range(10): # make 10K later
    start_time=time.time()
    game_list=[]
    # what you really just need to plot can be a List
    # I think.. This is an easier solution.
    round_counts=[]
    game = play_a_game(round_counts, game_list)
    game_list.append(game)
    
end_time=time.time()
print("Game list:", game_list)
print("Time takes {}.".format(end_time-start_time)) 


