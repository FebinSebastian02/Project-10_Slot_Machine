#imports are done
import random

#Global constants
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

#Design of Slot Machine
ROWS = 3
COLS = 3
#Symbols in each reel(column)
symbols = {"$": 3,
           "*": 4,
           "7": 6,
           "A": 8}  #Here, keys are the symbols and values are the number of symbols
def generateValuesInMachine(rows, cols, symbols):
    #Creating a list with all symbols
    reel = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):    #_ is an anonymous variable in Python used if we don't care about the variable
            reel.append(symbol)
    #Assigning symbols in a reel to every column
    columns = []    #This list have inner list that gives values in each column
    for _ in range(cols):   #Iterate through columns
        column = [] #To store values for each column
        copyReel = reel[:]  #Here, we are creating a copy of reel list by creating it's duplicate. If we don't give the
                            #slice operator "[:]", then both lists become same objects and if we change one, it affect other
        for _ in range(rows):   #Iterate through rows
            value = random.choice(copyReel)
            copyReel.remove(value)  #Once a value is selected,we should remove it from the list.
            column.append(value)
        columns.append(column)  #To store each column list.
    return columns

def printSlotMachine(columns):
    #Now, the columns list passed will have inner lists where the values will be present like rows even though those are
    #the values of column. So we need to convert those rows to columns. Here, we use a method called Transposing
    for row in range(len(columns)): #len(columns) gives the total no. of columns
          for i, col in enumerate(columns):   #We don't want to print | after last column. enumerate() gives index as well
                                              #as items in the collection.
              if i != len(columns) - 1: #len(columns) - 1 gives the maximum index position of columns list, i.e 2
                print(col[row], end=" | ")
              else:
                  print(col[row])

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
            print("\nCurrent Balance:- $", balance)
            while True:
                line = getNoOfLines()
                bet = getBet()
                totalBet = bet * line
                if totalBet <= balance:
                    print("\nEntered Lines:- ", line)
                    print("Placed Bet:- ", bet)
                    print(f"You are betting ${bet} on {line} line/lines. Total Bet placed:- ${totalBet}")
                    slots = generateValuesInMachine(ROWS, COLS, symbols)
                    print(slots)    #To be commented later
                    printSlotMachine(slots)
                else:
                    print(f"Insufficient balance. Your Current Balance:- ${balance}")
        elif choice == 2:
            pass
        else:
            print("Invalid option entered. Please enter a valid option...")

main()

