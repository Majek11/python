initialMessage = print("Which transaction do you want to perform?")

deposit = input("""
    1. Deposit
    2. Balance : #000.000
""")

match deposit:
    case 1: print("Press 1 to deposit")
    case 2: print("Press 2 to withdraw")

