#Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
def credit():
    while True:
        credit = int(input("\nEnter the amount that needs to be credited...$"))
        if credit <= 0:
            print("Invalid credit. Please enter a valid credit!")
        else:
            return credit

def getNoOfLines():
    while True:
        lines = int(input("\nEnter the number of lines(1-3) to bet on..."))
        if 1 <= lines <= 3:
            return lines
        else:
            print("Invalid number of lines entered. Please enter valid number of lines!")

def getBet():
    while True:
        bet = int(input("\nHow much would you like to bet on each line...$"))
        if MIN_BET <= bet <= MAX_BET:
            return bet
        else:
            print(f"Invalid bet amount entered. Please enter a valid amount to bet between {MIN_BET} and {MAX_BET}")
def main():
    print("\n!!!Welcome to the Slot Machine!!!")
    while True:
        choice = int(input("\nDo you wish to play...1) Yes 2) No"))
        if choice == 1:
            balance = credit()
            line = getNoOfLines()
            bet = getBet()
            totalBet = bet * line
            print("\nCurrent Balance:- $", balance)
            print("Entered Lines:- ", line)
            print("Placed Bet:- ", bet)
            print(f"You are betting ${bet} on {line} lines. Total Bet placed:- ${totalBet}")
        elif choice == 2:
            pass
        else:
            print("Invalid option entered. Please enter a valid option...")

main()

