import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
SLOT_SYMBOLS = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

VALUE_SYMBOLS = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def slot_machine_spin(rows, cols, symbols):
    symbols_list = []
    for sym, sym_count in symbols.items():
        for _ in range(sym_count):
            symbols_list.append(sym)
            
    columns = []
    for _ in range(rows):
        column = []
        current_symbol = symbols_list[:]
        for _ in range(cols):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
def print_slot_machine_spin(columns): #Transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") # column[row] is the key of transposing!
            else:
                print(column[row])
                
def check_winnings(columns, lines, bets, value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += (bets * value[symbol])
            winning_lines.append(line + 1)
    return winnings, winning_lines
    
def deposit():
    while True:
        amount = input("Please Deposit Your Money $")
        if amount.isdigit():
            money = int(amount)
            if money > 0:
                break
            else:
                print("Please Enter a positive Number")
        else:
            print("Please Enter a number")
    return money

def get_lines():
    while True:
        print("\nNOTE : 1 line means the Top line / 2 lines mean the Top and the Middle lines / 3 lines mean all lines")
        amount = input(f"How many lines do you want to bet on (1-{MAX_LINES})? : ")
        if amount.isdigit():
            lines = int(amount)
            if lines > 0:
                break
            else:
                print("There're only 3 lines")
        else:
            print("Please Enter a number")
    return lines

def get_bet():
    while True:
        amount = input("How Much Do you wanna bet on each lines $")
        if amount.isdigit():
            bets = int(amount)
            if MIN_BET <= bets <= MAX_BET:
                break
            else:
                print(f"Please bet between the range of {MIN_BET} and {MAX_BET}")
        else:
            print("Please Enter a number")
    return bets
def spin(balance):
    lines = get_lines()
    while True:
        bets = get_bet()
        total_bets = bets * lines
        if total_bets > balance:
            print(f"You don't have enough money, your current balance is ${balance}")
        else:
            break
    print(f"You're betting ${bets} on {lines} lines, your total bets is ${total_bets}")
    
    slots = slot_machine_spin(ROWS, COLS, SLOT_SYMBOLS)
    print_slot_machine_spin(slots)
    winnings, winning_lines = check_winnings(slots, lines, bets, VALUE_SYMBOLS)
    if winnings > 0:
        print(f"Congratz, You won ${winnings}")
        print("On lines :", *winning_lines)
    else:
        print("You lost! but You'll get it next time!")
    return winnings - total_bets

def main():
    balance = deposit()
    while True:
        play = input("Press ENTER to play (q to Quit) :")
        if play == "q":
            break
        balance += spin(balance)
        print(f"Your current balance is now ${balance}")
    print(f"Thank you for playing with us :), you're left with ${balance}")

main()