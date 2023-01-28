#Blackjack

import random

#establishing deck (52 cards),card, dealer and player hands

deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A'] #x4 for deck
playerHand=[]       #making list for participants hand via list for sequencing
dealerHand=[]

#dealing cards function
def dealCard(turn):
    card=random.choice(deck)    
    turn.append(card)
    deck.remove(card)

"""
dealCard(turn) is a function that takes a list (turn) as a parameter and deals a card from a deck of cards.

The function first chooses a random card from the deck using the choice() method. 
This random card is then appended to the list (turn) and removed from the deck.
Finally, the function returns the list (turn) with the new card added.

Parameters: 
turn - list of cards already in the turn

Returns: 
turn - list of cards with the newly dealt card added
"""

#calculating the total of hands for player/dealer, defining value of cards
def total(turn):
    total=0
    face=['J','Q','K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10                       
        else:       #For 'A' card scenario
            if total > 11:
                total += 1 
            else:
                total += 11 
    return total

"""
total(turn) is a function that takes in a list of cards and returns a total value based on the cards in the turn.

Parameters:
turn (list): a list of cards, which can be either numbers (1-10) or strings (J, Q, K, A)

Returns:
total (int): the total value of the cards in the turn

The function begins by setting the total value to 0. It then iterates through the list of cards, adding the corresponding value to the total:
- If the card is a number (1-10), the number is added to the total
- If the card is 'J', 'Q', or 'K', the value 10 is added to the total
- If the card is 'A', the value 1 or 11 is added to the total, depending on the current total:
    - If the current total is > 11, 1 is added to the total
    - If the current total is <= 11, 11 is added to the total

Once all the cards in the turn have been evaluated, the total value is returned. 
"""

#winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) >2:
        return dealerHand[0], dealerHand[1]

'''
revealDealerHand()

Description:
This function reveals the dealer's hand in a game of blackjack. 

Parameters:
None

Return Value:
If the dealer's hand has two cards, the function returns the first card. 
If the dealer's hand has more than two cards, the function returns the first two cards. 

Example Usage:
dealerHand = [3, 4, 7]
revealDealerHand()
# Returns (3, 4)

'''

#loops
for _ in range(2) :
    dealCard(dealerHand)
    dealCard(playerHand)
'''
This function is used to deal cards to both the dealer and the player.

The function begins by looping through the range 2, meaning it will run twice.

In each iteration, the function calls the dealCard() function, passing in the dealerHand and playerHand variables. 
The dealCard() function then deals a card to each hand, respectively.

'''


#testing
#print(dealerHand)
#print(playerHand)

playerIn=True
dealerIn=True

while playerIn or dealerIn:
    print(f"The dealer has {dealerHand[0]} and (X)")
    print(f"You have {playerHand} for a total of {total(playerHand)}")
    print(playerHand)
    if playerIn:
        stayOrHit=input("1: Stay\n 2: Hit\n")
    if total(dealerHand) >16:
        dealerIn= False
    else:
        dealCard(dealerHand)
       
    #scenario for player/ game end
    if stayOrHit == '1':
        playerIn = False    #player chooses option to STAY, game ends/ playerIn and dealerIn false, and score counts for all
        dealerIn= False     
    else:
        dealCard(playerHand)        #player chooses option to HIT, game continues and playerIn still runs
    if total(playerHand) >=21:
        break
    elif total(dealerHand) >=21:
        break
    
if total(playerHand) == 21:
    print(f"You have {playerHand} for a total of {total(playerHand)}! The dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Congratulations! You have blackjack!")
elif total(dealerHand) ==21:
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Dealer has a blackjack! The dealer wins.")
elif total(dealerHand) and total(playerHand) ==21:
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Push! The game is tied!")
elif total(playerHand) > 21:
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("You bust! Dealer wins.")
elif total(dealerHand)>21:
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)} ")
    print("Dealer busts! You win!!!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer wins!")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have{playerHand} for a total of {total(playerHand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")
