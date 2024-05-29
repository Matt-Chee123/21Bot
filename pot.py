class Pot:
    def __init__(self,balance=10000):
        self.balance = balance #total pot

    def bet(self,bet):
        self.balance -= bet

    def insurance_bet(self,bet):
        self.balance -= bet/2

    def double(self,bet):
        self.balance += bet
        bet *= 2
        self.balance -= bet


    def showBalance(self):
        print("Money Left: £", self.balance, " :)")
    def win(self,win):
        self.balance += win*2
    def insurance_win(self,win):
        self.balance += win*3

    def draw(self,bet):
        self.balance += bet



# all other casses come with the