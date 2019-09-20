import random
import time

def play_a_game(round_counts, game_list):
    start_time=time.time()
    game={}
    hands=0

    playerOneCards=list(range(1,11))
    playerTwoCards=list(range(1,11))

    # Play as long as this is true
    while len(playerOneCards) >= 0 or len(playerTwoCards) >= 0:
        # check the winner conditions
        if len(playerOneCards) == 0:
            print 'PlayerTwo won in this many hands:', hands
            return end_game(game, "PlayerTwo", hands, start_time)

        elif len(playerTwoCards) == 0:
            print 'PlayerOne won in this many hands:', hands
            return end_game(game, "PlayerOne", hands, start_time)
        else:
            play_a_hand(playerOneCards, playerTwoCards)
            hands += 1

def end_game(game, winner, hands, start_time):
    game["winner"] = "PlayerTwo"
    game["hands_played"] = hands
    game["time"] = time.time() - start_time
    game_list.append(game)
    round_counts.append(hands)

   
def play_a_hand(playerOneCards, playerTwoCards):
    playerOneHand = random.choice(playerOneCards)
    playerTwoHand = random.choice(playerTwoCards)
    print 'PlayerA is using {}.'.format(playerOneHand)
    print 'PlayerB is using {}.'.format(playerTwoHand)

    if playerOneHand == playerTwoHand:
        coin=random.choice(['front','back'])
               
        # Gotta love this fake ass coin.
        if coin == "front":
            print 'PlayerA wins coin flip'
            playerOneCards.append(playerOneHand)
            playerTwoCards.remove(playerOneHand)

        elif coin == "back":
            print 'PlayerB wins coin flip'
            playerOneCards.remove(playerTwoHand)
            playerTwoCards.append(playerTwoHand)
    
    elif playerOneHand > playerTwoHand:
        print 'PlayerA wins the hand'
        playerOneCards.append(playerTwoHand)
        playerTwoCards.remove(playerTwoHand)
            
    elif playerOneHand < playerTwoHand:
        print 'PlayberB wins the hand'
        playerOneCards.remove(playerOneHand)
        playerTwoCards.append(playerOneHand)

game_list=[]
round_counts=[]

for i in range(1000): # make 10K later
    game = play_a_game(round_counts, game_list)
    game_list.append(game)
    print "Game list:", game_list
    print "Round counts:", round_counts

