#!/usr/bin/env python3

#import all modules from db
from db import *
import random as r

MONEYFILE = "money.txt"
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
    topCard = deck.pop[0]
    return topCard

def main():
    choice = "y"

    while choice.lower() == "y":
        title()
        try:
            playerMoney = read_money_file(MONEYFILE)
            print(f"\nMoney: {playerMoney}")
        except:
            print("\nMoney file not found.")

        try:
            playerBetAmount = int(input("Bet amount: "))
            if playerBetAmount < 5 or playerBetAmount > 1000:
                continue
        except:
            print("Bet amount has to be greater than $5, and no more than $1000.")
                            
        print("\nDEALER'S SHOW CARD:")

        print("\nYOUR CARDS:")

        choice = input("\nPlay again (y/n): ")

    print("\nCome back soon!\nBye!")

if __name__ == "__main__":
    main()