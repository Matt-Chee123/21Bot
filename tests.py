import unittest
from bjSetup import BlackjackGame
from deck import Deck,Card

class TestBlackjack(unittest.TestCase):
    def test_dealer_hits_soft_17(self):
        # Create a game where the dealer is set up with a soft 17
        game = BlackjackGame()
        game.dealer_hand = [Card(11, 'Ace', 'Hearts'), Card(6, 'Six', 'Hearts')]
        game.player_hand = [Card(10, 'King', 'Diamonds'), Card(7, 'Seven', 'Diamonds')]

        # Force the dealer to stand, which should trigger a hit on soft 17
        game.stand()

        # Calculate the dealer's score after the method call
        dealer_score = game.calculate_score(game.dealer_hand)
        print(f"Dealer's final hand: {game.dealer_hand}, Score: {dealer_score}")

        # Check if the dealer indeed hit on a soft 17
        self.assertTrue(dealer_score > 17, "Dealer did hit on soft 17")
        self.assertGreater(len(game.dealer_hand), 2, "Dealer should not have 2 cards after hitting on soft 17")

    # Additional test to check the functionality
    def test_player_busts(self):
        game = BlackjackGame()
        game.player_hand = [Card(10, 'King', 'Clubs'), Card(9, 'Nine', 'Clubs'), Card(3, 'Three', 'Clubs')]
        self.assertTrue(game.calculate_score(game.player_hand) > 21, "Player should have busted")


    def test_insurance_win(self):
        game = BlackjackGame()
        game.player_hand = [Card(8,'Eight','Clubs'),Card(3,'Three','Spades')]
        game.dealer_hand = [Card(11, 'Ace','Hearts'),Card(10,'King','Clubs')]
        game.insurance_bet()
        self.assertTrue
if __name__ == "__main__":
    unittest.main()
