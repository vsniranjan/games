
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
# Definition of classes

class Card:

    def __init__ (self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__ (self):
        return f"{self.rank} of {self.suit}"

class Deck:

    def __init__ (self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))
    
    def shuffle(self):
        return random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()

class Hand:

    def __init__(self):
        self.cards = []
        self.score = 0
        self.aces = 0 

    def add_card(self,card):
        self.cards.append(card)
        self.score += card.value
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self, hand):
        if hand.score > 21 and self.aces > 0 :
            hand.score -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

# Function defintions

def take_bet(chips):
    
    print(f"You currently have {chips.total} chips")
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck, hand):
    current_card = deck.deal()
    hand.add_card(current_card)
    print(f"Added the {current_card.rank} of {current_card.suit}")
    hand.adjust_for_ace(hand)

def hit_or_stand(deck, hand):
    global playing
    acceptable_input = False
    while acceptable_input == False:
        choice = input(f"Your current score is {hand.score}, do you want to Hit or Stand: ")

        if choice == 'hit' or choice == 'h':
            hit(deck,hand)
            acceptable_input = True

        elif choice == 'stand' or choice == 's':
            playing = False
            acceptable_input = True

        else:
            print("Invalid input, try again!")

def show_some(player, dealer):

    print("PLAYER CARDS:", *player.cards, sep='\n ')
    print()
    print("DEALER'S CARDS:")
    print(" <card hidden>")
    print('',dealer.cards[1]) 

def show_all(player,dealer):
    
    print()
    print('----------------------------------')
    print("PLAYER CARDS:", *player.cards, sep='\n ')
    print("TOTAL SCORE: ", player.score)
    

    print('DEALER CARDS: ', *dealer.cards, sep='\n ' )
    print("TOTAL SCORE: ", dealer.score)
    print('----------------------------------')

    print()

def player_busts(player,dealer,chips):
    print()
    print()
    print("PLAYER BUSTS!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("DEALER BUSTS!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

    
chips = Chips()

while True:
    playing = True
    print("WELCOME TO BLACKJACK!!")
    print()

    current_deck = Deck()
    player = Hand()
    dealer = Hand()
    current_deck.shuffle()
    for i in range(2):
        player.add_card(current_deck.deal())
        dealer.add_card(current_deck.deal())


    take_bet(chips)    

    while playing:
        print()
        print('---------------------')
        print()
        show_some(player, dealer)
        print()
        hit_or_stand(current_deck, player)
        print()

        if player.score > 21:
            show_all(player, dealer)
            player_busts(player, dealer, chips)
            break
    

    if player.score <= 21:
        while dealer.score <= 17:
            dealer.add_card(current_deck.deal())
            if dealer.score > 21:
                show_all(player, dealer)
                dealer_busts(player, dealer, chips)
                break

    if player.score < 21 and dealer.score < 21:
        if player.score > dealer.score:
            show_all(player, dealer)
            player_wins(player, dealer, chips)

        elif dealer.score > player.score:
            show_all(player, dealer)
            dealer_wins(player, dealer, chips)

        else:
            show_all(player, dealer)
            push(player, dealer)
    
    print(f'You currently have {chips.total} chips remaining')

    if chips.total == 0:
        print("You don't have anymore chips to place a bet!")
        print("Game Over")
        break
    play_agn = input("Do you want to play again? (y/n): ")

    if play_agn == 'y':
        continue
    else:
        print("Thanks for playing!")
        if chips.total > 100:
            print(f"You walked away with a profit of ${chips.total - 100}")
        else:
            print(f"You walked away with a loss of ${100 - chips.total}")
        break
    
  
    