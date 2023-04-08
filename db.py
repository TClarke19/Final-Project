def read_money_file(MONEYFILE):
    with open(MONEYFILE) as file:
        file.read()

def write_money_file(MONEYFILE):
    with open(MONEYFILE, "w") as file:
        for amount in file:
            file.write(amount)