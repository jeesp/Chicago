import unittest
from entities.player import Player


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
        self.assertEqual(self.player.hand_value(), (52, 12))
    def test_new_player(self):
        self.player2 = Player("Aapo")
        self.assertEqual(self.player2.name, "Aapo")
        self.assertEqual(len(self.player2.hand), 0)
    def test_check_correct_straigth_with_ace(self):
        self.player.hand = [(14, 'spades', '4_of_spades'), (13, 'clubs', 'king_of_spades'), (
            12, 'spades', '5_of_clubs'), (11, 'spades', '8_of_spades'), (10, 'spades', '3_of_hearts')]
        numbers = []
        suits = set()
        for card in self.player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        self.assertEqual(self.player.check_straight_and_flush(suits, numbers), (4,14))
    def test_check_correct_straigth_from_one(self):
        self.player.hand = [(14, 'spades', '4_of_spades'), (3, 'clubs', 'king_of_spades'), (
            2, 'spades', '5_of_clubs'), (4, 'spades', '8_of_spades'), (5, 'spades', '3_of_hearts')]
        numbers = []
        suits = set()
        for card in self.player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        self.assertEqual(self.player.check_straight_and_flush(suits, numbers), (4,14))
    def test_check_failed_straight(self):
        self.player.hand = [(14, 'spades', '4_of_spades'), (13, 'clubs', 'king_of_spades'), (
            12, 'spades', '5_of_clubs'), (11, 'spades', '8_of_spades'), (9, 'spades', '3_of_hearts')]
        numbers = []
        suits = set()
        for card in self.player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        self.assertEqual(self.player.check_straight_and_flush(suits, numbers), None)
    def test_check_failed_straight_with_ace(self):
        self.player.hand = [(14, 'spades', '4_of_spades'), (13, 'clubs', 'king_of_spades'), (
            12, 'spades', '5_of_clubs'), (11, 'spades', '8_of_spades'), (14, 'spades', '3_of_hearts')]
        numbers = []
        suits = set()
        for card in self.player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        self.assertEqual(self.player.check_straight_and_flush(suits, numbers), None)

