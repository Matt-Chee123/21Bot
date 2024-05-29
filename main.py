from bjSetup import BlackjackGame
def main():
    game = BlackjackGame(1)
    deckChangeLim = 0.1*len(game.deck.cards)
    while len(game.deck.cards) > deckChangeLim:
        if game.pot.balance <= 0:
            print("Ran out of money, Failure")
            quit()
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        game.play()
        print(len(game.deck.cards))
    print('Games done, cards gone or ran out of money')



if __name__ == "__main__":
    main()