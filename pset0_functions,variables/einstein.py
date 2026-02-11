import random

suits = ["hearts" , "diamonds" , "spades" , "clubs"]

ranks = ["two" , "three" , "four" , "five" , "six" , "seven" , 
         "eight" , "nine" , "ten" , "jack" , "queen" , "king" , "ace"]

value = {"two" : 2 , "three" : 3 , "four" : 4 , "five" : 5 , 
         "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9 , 
         "ten" : 10 , "jack" : 10 , "queen" : 10 , "king" : 10 , "ace" : 11}
    
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def remove(self):
        return self.cards.pop()
    
    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

class Hand:
    def __init__(self):
        self.cards = []

    def receive(self, cards):
        self.cards.append(cards)

    def value(self):
        score = 0
        ace = 0 
        for card in self.cards:
            score += value[card.rank]
            if card.rank == "ace":
                ace += 1
        while score > 21 and ace > 0:
            score -= 10
            ace -= 1
        return score
    
    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

    
class Player:
    def __init__(self, name, balance):
        if not name:
            raise ValueError("missing name")
        self.name = name
        self.balance = balance
        self.hand = Hand()

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

    def bet(self, minbet, maxbet):
        while True:
            bet = input(f"Minimum bet is ${minbet} and maximum bet is ${maxbet}. How much would you like to bet? $")
            if bet.isdigit():
                bet = int(bet)
                if minbet <= bet <= maxbet:
                    if bet <= self.balance:
                        self.balance -= bet
                        print(f"Total bet: ${bet}. Current balance: ${self.balance}")
                        break
                    else:
                        print("Insufficient balance, please deposit more money.")
                        break
                else:
                    print(f"Betting amount must be between ${minbet} and ${maxbet}")
            else:
                print("Please enter a number.")
        return bet
    
    def new_hand(self):
        self.hand = Hand()

class Dealer(Player):
    def __init__(self):
        super().__init__(name="Dealer", balance=0)
        
    def show_first_card(self):
        return self.hand.cards[0]
    
class GameMaster:
    def __init__(self, minbet, maxbet):
        self.minbet = minbet
        self.maxbet = maxbet
        self.players = []
        self.dealer = Dealer()

    def add_player(self, player):
        self.players.append(player)

    def deal_cards(self, deck):
        self.dealer.new_hand()
        for player in self.players:
            player.new_hand()
        for _ in range(2):
            for player in self.players:
                player.hand.receive(deck.remove())
        self.dealer.hand.receive(deck.remove())

    def player_turn(self, deck, player):
        while player.hand.value() < 21:
            if value[player.hand.cards[0].rank] == value[player.hand.cards[1].rank]:
                action = input("Would you like to hit, stand, split or double down? ").strip().lower()
                if action == "split":
                    pass
                if action == "double down":
                    player.hand.receive(deck.remove)
                    break
                if action == "hit":
                    player.hand.receive(deck.remove)
                if action == "stand":
                    break
            else:
                action = input("Would you like to hit, stand or double down? ").strip().lower()
                if action == "double down":
                    player.hand.receive(deck.remove)
                    break
                if action == "hit":
                    player.hand.receive(deck.remove)
                if action == "stand":
                    break
        if player.hand.value() == 21:
            print("BLACKJACK!")



    def dealer_turn(self, deck):
        print(f"\n--- Dealer's Turn ---")
        print(f"Dealer reveals second card. \nHand: {self.dealer.hand} \nValue: {self.dealer.hand.value()}")
        while self.dealer.hand.value() < 17:
            print("Dealer hits...")
            self.dealer.hand.receive(deck.remove())
            print(f"Hand: {self.dealer.hand} \nValue: {self.dealer.hand.value()}")
            if self.dealer.hand.value() > 21:
                print("Dealer BUSTS!")

    def play_round(self, deck):
        for player in self.players:
            print(f"\n{player.name}'s turn to bet:")
            player.current_bet = player.bet(self.minbet, self.maxbet)
        self.deal_initial_cards(deck)
        for player in self.players:
            print(f"\n--- {player.name}'s Turn ---")
            self.player_turn(player, deck)
        self.dealer_turn(deck)

def main():
    gamemaster = GameMaster(minbet=1, maxbet=100)
    while True:
        number_of_players = input("How many players(Max 4)? ")
        if number_of_players.isdigit() and 1 <= int(number_of_players) <= 4:
            for number in number_of_players:
                name = input(f"Player {number}'s name: ")
                starting_amt = input("Please enter how much would you like to deposit. $")
                if starting_amt.isdigit():
                    starting_amt = int(starting_amt)
                    break
                else:
                    print("Please enter a positive whole number.")
                player = Player(name=name, balance=starting_amt)
                gamemaster.add_player(player)
            break
        else:
            print("Please enter a number between 1 and 4")
    

if __name__ == "__main__":
    main()