#pylint: disable=missing-docstring

"""
Blackjack Game

Plays a hand of blackjack against a dealer
Only has cards 1 - 10
"""

import sys
import random
import time
import os

print("Welcome to Blackjack")
print('-' * 50)

DECK_CONVERSION = {1:"Ace",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",
                    8:"8",9:"9",10:"X",11:"Jack",12:"Queen",13:"King","H":" "}

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

def select_card(current_deck):
    """
    Deals a card

    Returns a card but removes it from the 'deck'
    allowing probabilties to be correct
    """
    temp_deck = current_deck[:]
    place_holder = temp_deck.pop(random.randint(0,len(temp_deck) - 1))
    return place_holder, temp_deck

def initial_deal(current_deck): #assigns initial 2 cards to both players
    """
    Returns two cards to each 'player'
    """
    i = 0
    dealt_cards = []
    temp_deck = current_deck[:]
    while i < 4:
        place_holder, temp_deck = select_card(temp_deck[:])
        dealt_cards.append(place_holder)
        i += 1
    return dealt_cards[:2], dealt_cards[2:], temp_deck

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
        if total > 21 and contains_ace:
            total -= 10
            contains_ace = False
    return total

def card_string(*card_values):
    """
    Creates Pictorial Repersentation of Cards

    Takes in card values and returs an array
    of strings to repersent the cards
    """

    rows = ["", "", "", "", ""]
    for card in card_values:
        rows[0] += " -----\t"
        rows[1] += "|     |\t"
        rows[2] += f"|  {DECK_CONVERSION[card][0]}  |\t"
        rows[3] += "|     |\t"
        rows[4] += " -----\t"
    return rows

def draw_cards(dealer_card_shown):
    """
    Draws cards on the screen

    Using the returned array from the
    card_string function this function
    draws and erases the cards on the
    screen as required.
    """

    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")
    if not dealer_card_shown:
        for row in card_string(dealer_cards[0],"H"):
            print(row)
    else:
        for row in card_string(*dealer_cards):
            print(row)
    print("\n\n\n\n\n")
    for row in card_string(*player_cards):
        print(row)
    print(f"Player Total = {sum_cards(*player_cards)}")

while True:
    game_start = input("Do you want to start a new game? (y/n)").upper()
    if game_start == "N": #If player doesn't want to keep playing, exits
        sys.exit()
    if game_start != "Y": #If non valid input is entered, prints message and repeats loop
        print("Incorrect input, please enter y or n")
        continue

    deck = initialize_deck()
    dealer_cards, player_cards, deck = initial_deal(deck[:])

    draw_cards(False)

    while True:
        if sum_cards(*player_cards) == 21:
            print("Blackjack!")
            break
        player_action = input("Hit or stand? (h/s):").upper()
        if player_action == "S":
            break
        if player_action != "H":
            print("Incorrect input, please enter h or s")
            continue
        drawn_card, deck = select_card(deck[:])
        player_cards.append(drawn_card)
        draw_cards(False)
        if sum_cards(*player_cards) > 21:
            break
        if sum_cards(*player_cards) == 21:
            print("Blackjack!")
            break

    draw_cards(True)

    while True:
        if sum_cards(*player_cards) > 21:
            print("Dealer stands.")
            break
        if sum_cards(*dealer_cards) == 21:
            print("Dealer hit blackjack.")
            break
        if sum_cards(*dealer_cards) > 21:
            break
        if sum_cards(*dealer_cards) > 16:
            print("Dealer stands.")
            break
        drawn_card, deck = select_card(deck[:])
        dealer_cards.append(drawn_card)
        draw_cards(True)
        time.sleep(.75) #sleeps so dealer output isn't too quick


    if sum_cards(*player_cards) > 21:
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
