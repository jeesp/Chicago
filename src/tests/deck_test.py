import unittest
from entities.deck import Deck
from entities.player import Player


class TestDeck(unittest.TestCase):
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
    def test_dealing_from_dealt(self):
        players = []
        players.append(self.player)
        self.player.hand = [(3, 'hearts', '3_of_hearts')] 
        self.deck.cards = []
        self.deck.dealt_cards = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.deck.deal_cards(players)
        self.assertEqual(len(self.deck.cards), 0)
        self.assertEqual(len(self.player.hand), 5)
        self.assertEqual(len(self.deck.dealt_cards), 1)
    def test_add_card_to_dealt_cards(self):
        self.deck.add_card_to_dealt_cards((5,'spades', '5_of_spades'))
        self.assertEqual(len(self.deck.dealt_cards), 1)
