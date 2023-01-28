#Blackjack

import random

#establishing deck (52 cards),card, dealer and player hands

deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,'J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','A'] #x4 for deck
playerHand=[]       #making list for participants hand via list for sequencing
dealerHand=[]

#dealing cards function
def dealCard(turn):
    card=random.choice(deck)    #choice() method to to choose random element from list sequence of deck
    turn.append(card)
    deck.remove(card)

'''select random hand from deck, on turn take card from deck, and remove card from deck'''

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

#winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) >2:
        return dealerHand[0], dealerHand[1]

#loops
for _ in range(2) :
    dealCard(dealerHand)
    dealCard(playerHand)

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