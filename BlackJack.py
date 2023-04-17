#!/usr/bin/env python3

#import all modules from db and the random module built in to python
from db import *
import random as r

MONEYFILE = "money.txt" #file that records the amount of money the player has before and after playing

#Lists used to create a deck of cards
cardSuit = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardRank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#Function to display the title of the program
def title():
    print("\nBLACKJACK!\nBlackjack payout is 3:2")

#Function to create a new deck of cards and shuffle it each time the program starts
def deck_of_cards():
    deck = []
    for suit in cardSuit:
        for rank in cardRank:
            card = [rank + " of " + suit, rank, suit]
            deck.append(card)
            r.shuffle(deck)
    return deck

#Function to get the first card in the shuffled deck            
def get_top_card(deck):
    topCard = deck.pop(0)
    return topCard

#Function to calculate the value of the player's or the dealer's hand of cards
def calculate_hand(hand):
    total = 0
    for card in hand:
        if card[1].isdigit():
            total += int(card[1])
        elif card[1] in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            if (total + 11) > 21:
                total += 1
            else:
                total += 11
    return total

#The main function where the game is played and the main logic is contained
def main():
    choice = "y"

    while choice.lower() == "y":
        title()
        deck = deck_of_cards()
        #print(deck)
        playerHand = []
        playerCardOne = get_top_card(deck)
        playerCardTwo = get_top_card(deck)
        dealerHand = []
        dealerCard = get_top_card(deck)
        try:
            playerMoney = read_money_file(MONEYFILE)
            print(f"\nMoney: {playerMoney}")
        except FileNotFoundError:
            print("\nMoney file not found.")

        try:
            playerBetAmount = int(input("Bet amount: "))
            if playerBetAmount < 5 or playerBetAmount > 1000:
                continue
        except ValueError:
            print("Bet amount has to be greater than $5, and no more than $1000.")                        

        print("\nDEALER'S SHOW CARD:")
        print(dealerCard[0])

        print("\nYOUR CARDS:")
        playerHand.append(playerCardOne)
        playerHand.append(playerCardTwo)
        for card in playerHand:
            print(card[0])
        

        while True:
         choice = input("\nHit or stay? (hit/stay): ")
         if choice.lower() == "hit":
             playerHand.append(get_top_card(deck))
             print("\nYOUR CARDS:")
             for card in playerHand:
                 print(card[0])
             if calculate_hand(playerHand) > 21:
                 print("You bust!")
                 break
         elif choice.lower() == "stay":
             print("\nDEALER'S CARDS:")
             for card in dealerHand:
                 print(card[0])
             while calculate_hand(dealerHand) < 17:
                 dealerHand.append(get_top_card(deck))
                 print(f"\n{dealerHand[-1][0]}")
             if calculate_hand(dealerHand) > 21:
                 print("Dealer bust! You win!")
                 print(f"\nYour total: {calculate_hand(playerHand)}")
                 print(f"Dealer's total: {calculate_hand(dealerHand)}")
                 playerMoney += playerBetAmount * 1.5
                 write_money_file(MONEYFILE, playerMoney)
                 break
             elif calculate_hand(playerHand) > calculate_hand(dealerHand):
                 print("You win!")
                 print(f"\nYour total: {calculate_hand(playerHand)}")
                 print(f"Dealer's total: {calculate_hand(dealerHand)}")
                 playerMoney += playerBetAmount * 1.5
                 write_money_file(MONEYFILE, playerMoney)
                 break
             elif calculate_hand(playerHand) < calculate_hand(dealerHand):
                 print("Sorry. You lose.")
                 print(f"\nYour total: {calculate_hand(playerHand)}")
                 print(f"Dealer's total: {calculate_hand(dealerHand)}")
                 playerMoney -= playerBetAmount
                 write_money_file(MONEYFILE, playerMoney)
                 break
             else:
                 playerMoney += playerBetAmount
                 write_money_file(MONEYFILE, playerBetAmount)
                 break

        choice = input("\nPlay again (y/n): ")

    print("\nCome back soon!\nBye!")

if __name__ == "__main__":
    main()