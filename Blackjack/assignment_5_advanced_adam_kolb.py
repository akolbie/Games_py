#pylint: disable=missing-docstring

"""
Blackjack Game

Plays a hand of blackjack against a dealer
Only has cards 1 - 10
"""

import sys
import random
import time

print("Welcome to Blackjack")
print('-' * 50)

deck = []
DECK_CONVERSION = {1:"Ace",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",
                    8:"8",9:"9",10:"10",11:"Jack",12:"Queen",13:"King"}

def initialize_deck():
    """
    Creates a standard deck

    This allows the probability of drawing a card to
    change over time.
    """
    new_deck = []
    i = 0
    while i < 4:
        for j in range(1,14):
            new_deck.append(j)
        i += 1
    return new_deck

def select_card():
    """
    Deals a card

    Returns a card but removes it from the 'deck'
    allowing probabilties to be correct
    """
    global deck
    return deck.pop(random.randint(0,len(deck) - 1))

def initial_deal(): #assigns initial 2 cards to both players
    """
    Returns two cards to each 'player'
    """
    global deck
    return [select_card(), select_card()], [select_card(), select_card()]

def sum_cards(*args): #takes card values as inputs and sums them together
    """
    Calculates the sum of a hand

    Calculates the sum of a hand and
    adjusts an ace to be low if over 21
    """
    total = 0
    contains_ace = False
    for card in args:
        if card > 10:
            total += 10
        elif card == 1:
            total += 11
            contains_ace = True
        else:
            total += card
        if total > 21 and contains_ace == True:
            total -= 10
            contains_ace = False
    return total

while True:
    dealers_turn = True
    game_start = input("Do you want to start a new game? (y/n)").upper()
    if game_start == "N": #If player doesn't want to keep playing, exits
        sys.exit()
    if game_start != "Y": #If non valid input is entered, prints message and repeats loop
        print("Incorrect input, please enter y or n")
        continue
    
    deck = initialize_deck()
    dealer_cards, player_cards = initial_deal()
    print(f"You draw a {DECK_CONVERSION[player_cards[0]]} and a {DECK_CONVERSION[player_cards[1]]}.",
    f"Your total is {sum_cards(*player_cards)}")
    print(f"Dealer draws a {DECK_CONVERSION[dealer_cards[0]]} and a hidden card")

    while True:
        if sum_cards(*player_cards) == 21:
            print("Blackjack!")
            break
        player_action = input("Hit or stand? (h/s):").upper()
        if player_action == "S":
            dealers_turn = True
            break
        if player_action != "H":
            print("Incorrect input, please enter h or s")
            continue
        player_cards.append(select_card())
        print(f"You draw a {DECK_CONVERSION[player_cards[-1]]}. Your total is {sum_cards(*player_cards)}")
        if sum_cards(*player_cards) > 21:
            dealers_turn = False
            break


    if dealers_turn:
        print(f"Dealer's hidden card is a {DECK_CONVERSION[dealer_cards[-1]]}",
        f"and has a total of {sum_cards(*dealer_cards)}")

    while dealers_turn:
        if sum_cards(*dealer_cards) == 21:
            print("Dealer hit blackjack")
            break
        if sum_cards(*dealer_cards) > 21:
            break
        if sum_cards(*dealer_cards) > 16:
            print("Dealer stands.")
            break
        dealer_cards.append(select_card())
        print(f"Dealer hits and draws a {DECK_CONVERSION[dealer_cards[-1]]}.",
        f"Dealer's total is {sum_cards(*dealer_cards)}")
        time.sleep(.75) #sleeps so dealer output isn't too quick


    if not dealers_turn:
        print("You are bust, dealer wins")
    elif sum_cards(*dealer_cards) > 21:
        print("Dealer is bust, you win")
    elif sum_cards(*player_cards) > sum_cards(*dealer_cards):
        print("You win")
    elif sum_cards(*player_cards) == sum_cards(*dealer_cards):
        print("You and the dealer tie")
    else:
        print("Dealer wins")
    print("-" * 50)
