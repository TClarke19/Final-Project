#!/usr/bin/env python3

#import all modules from db
from db import *

MONEYFILE = "money.txt"

def title():
    print("\nBLACKJACK!\nBlackjack payout is 3:2")

def read_file(FILENAME):
    with open(FILENAME, "r") as file:
        contents = file.readlines()
        return contents

def main():
    choice = "y"

    while choice.lower() == "y":

        title()
        playerMoney = read_file(MONEYFILE)
        print(f"\nMoney; {playerMoney}")
        playerBetAmount = input("Bet amount: ")

        print("\nDEALER'S SHOW CARD:")

        print("\nYOUR CARDS:")

        choice = input("\nPlay again (y/n): ")

    print("\nCome back soon!\nBye!")

if __name__ == "__main__":
    main()