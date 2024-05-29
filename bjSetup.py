from deck import Deck
from pot import Pot
class BlackjackGame:


    ######config stuff
    def __init__(self,decks=1,starting_bet=10,total_money=1000):
        self.deck = Deck(decks)
        self.deck.shuffle()
        self.player_hand = []
        self.dealer_hand = []
        self.game_over = False
        self.pot = Pot(total_money)
        self.current_bet = 0
        self.insurance_bet = 0

    def deal_cards(self):
        self.player_hand = [self.deck.deal(),self.deck.deal()]
        self.dealer_hand = [self.deck.deal(),self.deck.deal()]



    def calculate_score(self,hand):
        score = 0
        ace_count = 0
        for card in hand:
            if card.name == 'Ace':
                ace_count += 1
                score += card.value
            else:
                score += card.value
        while score > 21 and ace_count > 0:
            score -= 10
            ace_count -= 1
        return score

    def check_soft_17(self,hand):
        score = 0
        soft = False
        for card in hand:
            score += card.value
            if card.name == 'Ace':
                soft = True
        if score == 17 and soft:
            return True
        else:
            return False



###### options funcs
    def stand(self,bet):
        if self.check_soft_17(self.dealer_hand):
            self.hit(self.dealer_hand)
        while self.calculate_score(self.dealer_hand) < 17:
            self.hit(self.dealer_hand)
            if self.check_soft_17(self.dealer_hand):
                self.hit(self.dealer_hand)
        print("Player's Hand: ", self.player_hand)
        print("Dealer's Hand: ", self.dealer_hand)
        player_score = self.calculate_score(self.player_hand)
        dealer_score = self.calculate_score(self.dealer_hand)
        return self.determine_winner(player_score,dealer_score,bet)

    def hit(self,hand):
        hand.append(self.deck.deal())
        if self.calculate_score(hand) > 21:
            return True
        return False
    def double_down(self):
        self.current_bet *= 2
        if self.hit(self.player_hand):
            print("Player's Hand: ", self.player_hand)
            print('Player Busts')
            self.game_over = True
        else:
            print('Players Hand after double down: ', self.player_hand)
        return True

    ###### bettings stuff

    def insurance_option(self):
        response = input('Would you like insurance?: (y/n) ')
        if response == 'y':
            print('Insurance taken, ', self.current_bet/2,' added as a sidebet for insurance')
            self.insurance_bet += self.current_bet/2
            self.pot.insurance_bet(self.current_bet)

    def insurance_win(self):
        self.pot.insurance_win(self.insurance_bet)



###### game play
    def play(self):
        print("GAME IS STARTING")
        self.pot.showBalance()
        self.bet()
        self.pot.bet(self.current_bet)
        self.deal_cards()
        print("Player's Hand: ", self.player_hand[0]," , ",self.player_hand[1])
        print("Dealer's Hand: ", self.dealer_hand[0]," , Hidden")
        if self.dealer_hand[0].name == 'Ace':
            self.insurance_option()
        while True:
            if len(self.player_hand) == 2:
                action = input("Hit, Stick or Double Down: ")
            else:
                action = input("Hit or Stick: ")
            if action == 'Hit' or action == 'hit':
                if self.hit(self.player_hand):
                    print("Player's Hand: ", self.player_hand)
                    print("Player Busts! Dealer wins")
                    break
                print("Player's Hand: ", self.player_hand)
            elif action == 'Stick' or action == 'stick':
                self.stand(self.current_bet)
                if self.insurance_bet != 0 and len(self.dealer_hand) == 2 and self.calculate_score(self.dealer_hand) == 21:
                    print("Dealer BlackJack")
                    self.pot.insurance_win(self.insurance_bet)
                    self.insurance_bet = 0
                break
            elif action == 'Double Down' or action == 'double down':
                print(self.current_bet)
                self.pot.double(self.current_bet)
                print(self.current_bet)
                self.double_down()
                self.stand(self.current_bet)
                break
            else:
                print("Invalid input")


    def determine_winner(self,pHand,dHand,bet):
        print(bet)
        if pHand > 21:
            print('Player busts. Dealer Wins')
        elif dHand > 21:
            print('Dealer busts. Player Wins')
            self.pot.win(bet)
        elif pHand < dHand:
            print('Dealer beats player')
        elif dHand < pHand:
            print('Player beats dealer')
            self.pot.win(bet)
        else:
            print('Push. Draw')
            self.pot.draw(bet)


#Betting stuff

    def bet(self):
        self.current_bet = 0
        self.current_bet = int(input("How much would you like to bet?: (£)"))
        while self.pot.balance - self.current_bet < 0:
            print("Insufficient funds for that bet")
            print("Max bet you can afford is: ", self.pot.balance)
            self.current_bet = int(input("How much would you like to bet?: (£)"))

