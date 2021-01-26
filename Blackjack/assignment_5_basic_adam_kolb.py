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

def initial_deal(): #assigns initial 2 cards to both players
    return [random.randint(1,10),random.randint(1,10)], [random.randint(1,10),random.randint(1,10)]

def sum_cards(*args): #takes card values as inputs and sums them together
    total = 0
    for card in args:
        total += card
    return total

while True:
    dealers_turn = True
    game_start = input("Do you want to start a new game? (y/n)").upper()
    if game_start == "N": #If player doesn't want to keep playing, exits
        sys.exit()
    if game_start != "Y": #If non valid input is entered, prints message and repeats loop
        print("Incorrect input, please enter y or n")
        continue

    dealer_cards, player_cards = initial_deal()
    print(f"You draw a {player_cards[0]} and a {player_cards[1]}.",
    f"Your total is {sum_cards(*player_cards)}")
    print(f"Dealer draws a {dealer_cards[0]} and a hidden card")

    while True:
        player_action = input("Hit or stand? (h/s):").upper()
        if player_action == "S":
            dealers_turn = True
            break
        if player_action != "H":
            print("Incorrect input, please enter h or s")
            continue
        player_cards.append(random.randint(1,10))
        print(f"You draw a {player_cards[-1]}. Your total is {sum_cards(*player_cards)}")
        if sum_cards(*player_cards) > 21:
            dealers_turn = False
            break
        if sum_cards(*player_cards) == 21:
            print("Blackjack!")
            break

    if dealers_turn:
        print(f"Dealer's hidden card is a {dealer_cards[-1]}",
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
        dealer_cards.append(random.randint(1,10))
        print(f"Dealer hits and draws a {dealer_cards[-1]}.",
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
