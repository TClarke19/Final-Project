#!/usr/bin/env python3

#import all modules from db
from db import *

MONEYFILE = "money.txt"

def title():
    print("\nBLACKJACK!\nBlackjack payout is 3:2")

def main():
    choice = "y"

    while choice.lower() == "y":

        title()
        playerMoney = read_money_file(MONEYFILE)
        print(f"\nMoney; {playerMoney}")
        playerBetAmount = input("Bet amount: ")

        print("\nDEALER'S SHOW CARD:")

        print("\nYOUR CARDS:")

        choice = input("\nPlay again (y/n): ")

    print("\nCome back soon!\nBye!")

if __name__ == "__main__":
    main()