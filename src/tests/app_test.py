import unittest
from player import Player
from deck import Deck
import app
class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jake")
        self.player2 = Player("Make")
        self.player3 = Player("Ake")

    def test_comparing_nothing(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (0, 0, 0))
    def test_comparing_pair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (self.player, 1, 0))
    def test_comparing_twopair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (4, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (0, 1, 2))
    def test_comparing_better_pair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (self.player2, 1, 1))
    def test_comparing_three_of_a_kind(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (4, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (self.player, 3, 0))

    
    def compare(self, hand_value1, hand_value2, hand_value3):
        hands = []
        hands.append((self.player, hand_value1))
        hands.append((self.player2, hand_value2))
        hands.append((self.player3, hand_value3))
        return app.compare_hands(hands)
        
    
        
