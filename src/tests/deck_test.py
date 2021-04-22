import unittest
from deck import Deck
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.player = Player("Jake")

    def test_default_deck(self):
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        cards = []
        for suit in suits:
            for number in numbers:
                if number == 14:
                    number_string = 'ace'
                else:
                    number_string = str(number)
                cards.append((number, suit, number_string+"_of_"+suit))
        self.assertEqual(len(self.deck.cards), len(cards))
        self.assertEqual(len(self.deck.dealt_cards), 0)

    def test_dealing_card(self):
        players = []
        players.append(self.player)
        self.deck.deal_cards(players)
        self.assertEqual(len(self.deck.cards), 47)
        self.assertEqual(len(self.player.hand), 5)
        self.assertEqual(len(self.deck.dealt_cards), 0)
