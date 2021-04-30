import unittest
from entities.player import Player
from entities.deck import Deck
from game_actions import end_game_poker_comparison, play_poker, play_trick, compare_hands, end_trick, set_compare_card
from game_actions import play_card, round_ending


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Jake")
        self.player2 = Player("Make")
        self.player3 = Player("Ake")
        self.scoreboard = {self.player: 0, self.player2: 0, self.player3: 0}
        self.hand_values = {0: "Ei mitään", 1: "Pari", 2: "Kaksi paria", 3: "Kolmoset", 4: "Suora",
                   5: "Väri", 6: "Täyskäsi", 8: "Neloset", 10: "Värisuora"}
        self.compare_card = None
        self.played_cards = []
        self.value_comparison = (0,0,0)
        self.players = [self.player, self.player2, self.player3]
        self.winningtext = []

    def test_set_compare_card(self):
        card = (5, 'spades', self.player3)
        set_compare_card(self, self.player3, card)
        self.assertEqual(self.compare_card, (5,'spades',self.player3))
    def test_play_first_card(self):
        self.compare_card = None
        played_card = (5, 'spades', self.player3)
        self.player3.hand.append(played_card)
        self.assertEqual(len(self.player3.hand), 1)
        play_card(self, self.player3, played_card)
        self.assertEqual(self.compare_card, played_card)
        self.assertEqual(len(self.player3.hand), 0)
    def test_play_first_card(self):
        self.compare_card = (2, 'spades', self.player2)
        played_card = (5, 'spades', self.player3)
        self.player3.hand.append(played_card)
        self.assertEqual(len(self.player3.hand), 1)
        play_card(self, self.player3, played_card)
        self.assertEqual(self.compare_card, played_card)
        self.assertEqual(len(self.player3.hand), 0)
    def test_play_losing_card(self):
        self.compare_card = (5, 'spades', self.player3)
        played_card = (2, 'spades', self.player2)
        self.player2.hand.append(played_card)
        play_card(self, self.player2, played_card)
        self.assertEqual(self.compare_card, (5, 'spades', self.player3))
        self.assertEqual(len(self.player3.hand), 0)
    def test_play_wrong_suit_card(self):
        self.compare_card = (5, 'spades', self.player3)
        played_card = (2, 'clubs', self.player2)
        self.player2.hand.append(played_card)
        play_card(self, self.player2, played_card)
        self.assertEqual(self.compare_card, (5, 'spades', self.player3))
        self.assertEqual(len(self.player3.hand), 0)
    def test_round_ending(self):
        chicago = dict()
        for player in self.players:
            chicago[player] = 0
        self.scoreboard[self.player3] = 11
        self.assertEqual(round_ending(self, chicago), True)
        self.assertEqual(len(self.winningtext), 2)
        self.assertEqual(self.winningtext[0], "Peli päättynyt!")
        self.assertEqual(self.winningtext[1], "Voittaja on: " + self.player3.name 
                         + ". Pisteet: " + str(self.scoreboard[self.player3]))
    def test_points_check(self):
        x = 0
    def test_end_game_poker(self):
        self.assertEqual(end_game_poker_comparison(self), "Kenelläkään ei ollut mitään, joten kukaan ei saanut lopun pokeripisteitä.")
    def test_end_trick_succesful_blanco(self):
        chicago_on = True
        chicago_successful = True
        chicago_player = self.player3
        blanco_is_on = True
        self.compare_card = (5, 'spades', self.player3)
        end_trick(self, chicago_on, chicago_successful, chicago_player,
                  blanco_is_on)
        self.assertEqual(
            (self.scoreboard[self.player3], self.scoreboard[self.player2]), (30, 0))

    def test_end_trick_unsuccesful_chicago(self):
        chicago_on = True
        chicago_successful = False
        chicago_player = self.player3
        blanco_is_on = False
        self.compare_card = (5, 'spades', self.player2)
        end_trick(self, chicago_on, chicago_successful, chicago_player,
                  blanco_is_on)
        self.assertEqual(
            (self.scoreboard[self.player3], self.scoreboard[self.player2]), (-15, 5))

    def test_end_trick_unsuccesful_blanco(self):
        chicago_on = True
        chicago_successful = False
        chicago_player = self.player3
        blanco_is_on = True
        self.compare_card = (5, 'spades', self.player2)
        end_trick(self, chicago_on, chicago_successful, chicago_player,
                  blanco_is_on)
        self.assertEqual(
            (self.scoreboard[self.player3], self.scoreboard[self.player2]), (-30, 5))

    def test_end_trick_no_chicago(self):
        chicago_on = False
        chicago_successful = False
        chicago_player = None
        blanco_is_on = False
        self.compare_card = (5, 'spades', self.player2)
        end_trick(self, chicago_on, chicago_successful, chicago_player,
                  blanco_is_on)
        self.assertEqual(
            (self.scoreboard[self.player3], self.scoreboard[self.player2]), (0, 5))

    def test_end_trick_with_2_no_chicago(self):
        chicago_on = False
        chicago_successful = False
        chicago_player = None
        blanco_is_on = False
        self.compare_card = (2, 'spades', self.player2)
        end_trick(self, chicago_on, chicago_successful, chicago_player,
                  blanco_is_on)
        self.assertEqual(
            (self.scoreboard[self.player3], self.scoreboard[self.player2]), (0, 10))

    def test_comparing_nothing(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (0, 0, 0))

    def test_comparing_pair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player, 1, 0))

    def test_comparing_twopair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(4, 'diamonds', '4_of_spades'), (4, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(self, hv1, hv2, hv3), (0, 1, 2))

    def test_comparing_better_pair(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player2, 1, 1))

    def test_comparing_three_of_a_kind(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            4, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player, 3, 0))
    def test_comparing_straight_flush(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(8, 'spades', '8_of_spades'),]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player, 10, 0))
    def test_comparing_straight(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(8, 'clubs', '8_of_clubs'),]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player, 4, 0))

    def test_comparing_flush(self):
        self.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(9, 'spades', '9_of_spades'),]
        self.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.player.hand_value()
        hv2 = self.player2.hand_value()
        hv3 = self.player3.hand_value()
        self.assertEqual(TestPlayer.compare(
            self, hv1, hv2, hv3), (self.player, 5, 0))
    def compare(self, hand_value1, hand_value2, hand_value3):
        hands = []
        hands.append((self.player, hand_value1))
        hands.append((self.player2, hand_value2))
        hands.append((self.player3, hand_value3))
        return compare_hands(hands)
