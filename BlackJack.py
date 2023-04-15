#!/usr/bin/env python3

#import all modules from db
from db import *
import random as r

MONEYFILE = "D:\CNA ASD\Winter 2023\CP1856 Programming with Python\Final Project\money.txt"
#CARDFILE = "cards.txt"

cardSuit = ["Hearts", "Diamonds", "Clubs", "Spades"]
cardRank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardValue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def title():
    print("\nBLACKJACK!\nBlackjack payout is 3:2")

def read_file(FILENAME):
    with open(FILENAME, "r") as file:
        contents = file.readlines()
        return contents

def deck_of_cards():
    deck = []
    for suit in cardSuit:
        for rank in cardRank:
            card = [rank + " of " + suit, rank, suit]
            deck.append(card)
            r.shuffle(deck)
            return deck
            
def get_top_card(deck):
    if deck:
        topCard = deck.pop(0)
        return topCard
    else:
        return None

def calculate_hand(hand):
    total = 0
    for card in hand:
        if card[1].isdigit():
            total += int(card[1])
        elif card[1] in ['Jack', 'Queen', 'King']:
            total += 10
        else:
            if total + 11 > 21:
                total += 1
            else:
                total += 11
    return total

def main():
    playerHand = []
    dealerHand = []
    choice = "y"

    while choice.lower() == "y":
        title()
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
                            
        deck = deck_of_cards()
        playerCardOne = get_top_card(deck)
        playerCardTwo = get_top_card(deck)
        dealerCard = get_top_card(deck)

        print("\nDEALER'S SHOW CARD:")
        print(dealerCard[0])

        print("\nYOUR CARDS:")
        for card in playerHand:
            print(card[0])

        while True:
         choice = input("\nHit or stay? (hit/stay): ")
         if choice.lower() == "hit":
             playerHand.append(get_top_card(deck))
             print("YOUR CARDS:")
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
                 break
             else:
                 playerMoney += playerBetAmount
                 write_money_file(MONEYFILE, playerMoney)
                 break

        choice = input("\nPlay again (y/n): ")

    print("\nCome back soon!\nBye!")

if __name__ == "__main__":
    main()