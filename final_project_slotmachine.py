import random

symbol_and_count = {
    "🍒" : 35, #35%
    "🍋" : 22, #22%
    "🍊" : 15, #15%
    "🍇" : 11, #11%
    "🔔" : 9, #9%
    "🍀" : 8 #8%
}

symbol_and_multiplier = {
    "🍒": {3:5 , 4:10 , 5:30},
    "🍋": {3:10 , 4:20 , 5:80},
    "🍊": {3:15 , 4:40 , 5:250},
    "🍇": {3:25 , 4:120 , 5:800},
    "🔔": {3:50 , 4:250 , 5:3000},
    "🍀": {3:120 , 4:800 , 5:12000}
}

#current rtp about 88%

paylines = [
    [1,1,1,1,1], # middle straight
    [0,0,0,0,0], # top straight
    [2,2,2,2,2], # bottom straight
    [0,0,1,2,2], # diagonal top left to bottom right
    [2,2,1,0,0], # diagonal bottom left to top right
    [0,1,2,1,0], # v shape
    [2,1,0,1,2], # inverted v shape
    [0,2,0,2,0], # w shape
    [2,0,2,0,2]  # m shape
]

class Player:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amt):
        if amt.isdigit():
            amt = int(amt)
            self.balance += amt
            print(f"Amount deposited: ${amt}. Current balance: ${self.balance}")
        else:
            print("Please enter a positive whole number.")

    def withdraw(self, amt):
        if amt.isdigit(): 
            amt = int(amt)
            if self.balance - amt >= 0:
                self.balance -= amt
                print(f"Amount withdrawn: ${amt}. Current balance: ${self.balance}")
            else:
                print(f"Insufficent balance. Current balance: ${self.balance}")        
        else:
            print("Please enter a positve whole number.")

class Slotmachine:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.symbols = []
        for symbol , count in symbol_and_count.items():
            for _ in range(count):
                self.symbols.append(symbol)
        
    def spin(self):
        grid = []
        for _ in range(self.columns):
            column = []
            for _ in range(self.rows):
                value = random.choice(self.symbols)
                column.append(value)
            grid.append(column)
        return grid

    def print(self, grid):
        for row in range(self.rows):
            for i, col in enumerate(grid):
                if i != len(grid) - 1:
                    print(col[row], end = " | ")
                else:
                    print(col[row])

class Gamematser:
    def __init__(self, maxlines, minbet, maxbet):
        self.maxlines = maxlines
        self.minbet = minbet
        self.maxbet = maxbet

    def lines(self, player):
        while True:
            lines = input(f"How many lines would you like to bet on (1 - {self.maxlines})? ")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self.maxlines:
                    if lines <= player.balance:                       
                        break
                    else:
                        print(f"Minimum bet is $1. Betting on current number of lines would exceed the amount left in the balance. Current balance: ${player.balance}.")
                        break
                else:
                    print(f"Lines must be between 1 and {self.maxlines}.")
            else:
                print(f"Please enter a number between 1 and {self.maxlines}.")
        return lines

    def bet(self, lines, player):
        while True:
            bet = input("How much would you like to bet per line? $")
            if bet.isdigit():
                bet = int(bet)
                if self.minbet <= bet <= self.maxbet:
                    total_bet = bet * lines
                    if total_bet <= player.balance:
                        player.balance -= total_bet
                        print(f"Total bet: ${total_bet}. Current balance: ${player.balance}")
                        break
                    else:
                        print("Insufficient balance, please deposit more money.")
                        break
                else:
                    print(f"Betting amount must be between ${self.minbet} and ${self.maxbet}")
            else:
                print("Please enter a number.")
        return bet

    def winning(self, grid, lines, bet, player):
        winnings = 0
        for i in range(lines):
            check_for_pattern = paylines[i]
            symbol_on_line = [grid[col][check_for_pattern[col]] for col in range(5)]
            match_count = 1
            for symbol in symbol_on_line[1:]:
                if symbol == symbol_on_line[0]:
                    match_count += 1
                else:
                    break
            if match_count >= 3:
                multiplier = symbol_and_multiplier[symbol_on_line[0]].get(match_count, 0)
                winnings += multiplier * bet       
        player.balance += winnings
        print(f"Total amount won: ${winnings}. Current balance: ${player.balance}")

def main():
    slotmachine = Slotmachine(rows=3, columns=5)
    gamemaster = Gamematser(maxlines=9, minbet=1, maxbet=100)
    while True:
        starting_amt = input("Please enter how much would you like to deposit. (Note: minimum bet is $10) $")
        if starting_amt.isdigit():
            starting_amt = int(starting_amt)
            break
        else:
            print("Please enter a positive whole number.")
    player = Player(balance=starting_amt)
    while True:
        action = input("What would you like to do? Deopsit, Withdraw, Spin or End? ").strip().lower()
        if action == "deposit":
            deposit_amount = input("How much would you like to deposit? $")
            player.deposit(amt=deposit_amount)
            continue
        if action == "withdraw":
            withdraw_amount = input("How much would you like to withdraw? $")
            player.withdraw(amt=withdraw_amount)
            continue
        if action == "spin":
            number_of_betting_lines = gamemaster.lines(player=player)
            bet_per_line = gamemaster.bet(lines=number_of_betting_lines, player=player)
            grid_after_spin = slotmachine.spin()
            slotmachine.print(grid=grid_after_spin)
            gamemaster.winning(grid=grid_after_spin, lines=number_of_betting_lines, bet=bet_per_line, player=player)
        if action == "end":
            print(f"Amount cashed out: ${player.balance}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
