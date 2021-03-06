import random

class Deck:
    """
    Luokka pakalle, konstruktori luo kaikki kortit listaan ja luo jaettujen korttien pakan.
    """
    def __init__(self):
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        cards = []
        for suit in suits:
            for number in numbers:
                if number == 14:
                    number_string = 'ace'
                elif number == 13:
                    number_string = 'king'
                elif number == 12:
                    number_string = 'queen'
                elif number == 11:
                    number_string = 'jack'
                else:
                    number_string = str(number)
                cards.append((number, suit, number_string+"_of_"+suit))
        self.cards = cards
        self.dealt_cards = []
    def add_card_to_dealt_cards(self, card):
        """
        Metodi korttien lisäämiseksi jaettuihin kortteihin.
        """
        self.dealt_cards.append(card)
    def deal_cards(self, players):
        """
        Metodi korttien jakamiseen pelaajille.
        """
        for player in players:
            while len(player.hand) < 5:
                if len(self.cards) > 0:
                    card = self.cards[0]
                    self.cards.remove(card)
                    player.hand.append(card)
                else:
                    card = random.choice(self.dealt_cards)
                    self.dealt_cards.remove(card)
                    player.hand.append(card)
