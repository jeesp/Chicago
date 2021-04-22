import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jake")

    def test_hand_value(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (0, 0))

        self.player.hand = [(13, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (1, 13))

        self.player.hand = [(13, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            8, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (2, 0))

        self.player.hand = [(13, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            13, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (3, 13))

        self.player.hand = [(9, 'spades', '4_of_spades'), (10, 'spades', 'king_of_spades'), (
            12, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (11, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (4, 12))

        self.player.hand = [(4, 'spades', '4_of_spades'), (7, 'spades', 'king_of_spades'), (
            2, 'spades', '5_of_clubs'), (13, 'spades', '8_of_spades'), (3, 'spades', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (5, 13))

        self.player.hand = [(13, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            13, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (8, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (6, 1))

        self.player.hand = [(13, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            13, 'clubs', '5_of_clubs'), (13, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (8, 13))

        self.player.hand = [(9, 'spades', '4_of_spades'), (10, 'spades', 'king_of_spades'), (
            12, 'spades', '5_of_clubs'), (8, 'spades', '8_of_spades'), (11, 'spades', '3_of_hearts')]
        self.assertEqual(self.player.hand_value(), (10, 12))
