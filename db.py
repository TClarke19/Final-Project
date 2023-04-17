def read_money_file(MONEYFILE):
    with open(MONEYFILE) as file:
        amount = float(file.read())
    return amount

def write_money_file(MONEYFILE, amount):
    with open(MONEYFILE, "w") as file:
        file.write(str(amount))