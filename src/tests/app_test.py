import unittest
from entities.player import Player
from entities.deck import Deck
from game_logic.game_actions import App


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.player = Player("Jake")
        self.app.player2 = Player("Make")
        self.app.player3 = Player("Ake")
        self.app.scoreboard = {self.app.player: 0, self.app.player2: 0, self.app.player3: 0}
        self.app.hand_values = {0: "Ei mitään", 1: "Pari", 2: "Kaksi paria", 3: "Kolmoset", 4: "Suora",
                           5: "Väri", 6: "Täyskäsi", 8: "Neloset", 52: "Värisuora"}
        self.app.compare_card = None
        self.app.played_cards = []
        self.app.value_comparison = (0, 0, 0)
        self.app.players = [self.app.player, self.app.player2, self.app.player3]
        self.app.winningtext = []
        self.app.deck = Deck()
        self.app.round_ending_lines = []
        self.app.poker_hand_lines = []
        self.app.chicago = dict()
        self.app.chicago_on = False
        self.app.chicago_successful = False
        self.app.chicago_player = False
        self.app.blanco_is_on = False
        self.app.deals = 0
    def test_change_card(self):
        player = self.app.player3
        self.app.player3.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        cards_clicked = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades')]
        self.assertEqual(len(self.app.player3.hand), 5)
        self.assertEqual(len(self.app.deck.dealt_cards), 0)
        self.app.change_card(player, cards_clicked)
        self.assertEqual(len(self.app.player3.hand), 3)
        self.assertEqual(len(self.app.deck.dealt_cards), 2)
    def test_set_compare_card(self):
        card = (5, 'spades', self.app.player3)
        self.app.set_compare_card(self.app.player3, card)
        self.assertEqual(self.app.compare_card, (5,'spades',self.app.player3))
    def test_set_up_players(self):
        self.app.set_up_players()
        self.assertEqual(len(self.app.players), 4)
    def test_set_up_scoreboard(self):
        self.app.set_up_scoreboard()
        self.assertEqual(len(self.app.scoreboard), 3)
    def test_play_first_card(self):
        self.app.compare_card = None
        played_card = (5, 'spades', self.app.player3)
        self.app.player3.hand.append(played_card)
        self.assertEqual(len(self.app.player3.hand), 1)
        self.app.play_card(self.app.player3, played_card)
        self.assertEqual(self.app.compare_card, played_card)
        self.assertEqual(len(self.app.player3.hand), 0)
    def test_play_winning_card(self):
        self.app.compare_card = (2, 'spades', self.app.player2)
        played_card = (5, 'spades', self.app.player3)
        self.app.player3.hand.append(played_card)
        self.assertEqual(len(self.app.player3.hand), 1)
        self.app.play_card(self.app.player3, played_card)
        self.assertEqual(self.app.compare_card, played_card)
        self.assertEqual(len(self.app.player3.hand), 0)
    def test_play_losing_card(self):
        self.app.compare_card = (5, 'spades', self.app.player3)
        played_card = (2, 'spades', self.app.player2)
        self.app.player2.hand.append(played_card)
        self.app.play_card(self.app.player2, played_card)
        self.assertEqual(self.app.compare_card, (5, 'spades', self.app.player3))
        self.assertEqual(len(self.app.player3.hand), 0)
    def test_play_wrong_suit_card(self):
        self.app.compare_card = (5, 'spades', self.app.player3)
        played_card = (2, 'clubs', self.app.player2)
        self.app.player2.hand.append(played_card)
        self.app.play_card(self.app.player2, played_card)
        self.assertEqual(self.app.compare_card, (5, 'spades', self.app.player3))
        self.assertEqual(len(self.app.player3.hand), 0)
    def test_round_ending(self):
        self.app.deals = 3
        self.app.value_comparison = (0, 1, 2)
        self.app.scoreboard[self.app.player3] = 100
        self.assertEqual(self.app.round_ending(), True)
        self.assertEqual(len(self.app.winningtext), 2)
        self.assertEqual(self.app.winningtext[0], "Peli päättynyt!")
        self.assertEqual(self.app.winningtext[1], "Voittaja on: " + self.app.player3.name
                         + ". Pisteet: " + str(self.app.scoreboard[self.app.player3]))
    def test_points_check(self):
        x = 0
    def test_end_game_poker_with_nothing(self):
        self.app.deals = 3
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_end_game_poker_with_clear_winner(self):
        self.app.value_comparison = (self.app.player3, 1, 0)
        self.app.deals = 3
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_end_game_poker_win_with_same_hand(self):
        self.app.value_comparison = (self.app.player3, 1, 1)
        self.app.deals = 3
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 3)
    def test_end_game_poker_draw_same_hand(self):
        self.app.value_comparison = (0, 1, 2)
        self.app.deals = 3
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_poker_points_with_clear_winner(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_poker_points_no_points(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_poker_points_win_same_hand(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(3, 'spades', '4_of_spades'), (3, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (6, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 3)
    def test_poker_points_same_hand(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.poker_points()
        self.assertEqual(len(self.app.poker_hand_lines), 2)
    def test_end_trick_succesful_blanco(self):
        self.app.chicago_on = True
        self.app.chicago_successful = True
        self.app.chicago_player = self.app.player3
        self.app.blanco_is_on = True
        self.app.compare_card = (5, 'spades', self.app.player3)
        self.app.end_trick()
        self.assertEqual(
            (self.app.scoreboard[self.app.player3], self.app.scoreboard[self.app.player2]), (30, 0))

    def test_end_trick_unsuccesful_chicago(self):
        self.app.chicago_on = True
        self.app.chicago_player = self.app.player3
        self.app.compare_card = (5, 'spades', self.app.player2)
        self.app.end_trick()
        self.assertEqual((self.app.scoreboard[self.app.player3], self.app.scoreboard[self.app.player2]), (-15, 5))

    def test_end_trick_unsuccesful_blanco(self):
        self.app.chicago_on = True
        self.app.chicago_player = self.app.player3
        self.app.blanco_is_on = True
        self.app.compare_card = (5, 'spades', self.app.player2)
        self.app.end_trick()
        self.assertEqual((self.app.scoreboard[self.app.player3], self.app.scoreboard[self.app.player2]), (-30, 5))

    def test_end_trick_no_chicago(self):
        self.app.compare_card = (5, 'spades', self.app.player2)
        self.app.end_trick()
        self.assertEqual((self.app.scoreboard[self.app.player3], self.app.scoreboard[self.app.player2]), (0, 5))

    def test_end_trick_with_2_no_chicago(self):
        self.app.compare_card = (2, 'spades', self.app.player2)
        self.app.end_trick()
        self.assertEqual(
            (self.app.scoreboard[self.app.player3], self.app.scoreboard[self.app.player2]), (0, 10))

    def test_comparing_nothing(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (13, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (0, 0, 0))

    def test_comparing_pair(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player, 1, 0))

    def test_comparing_twopair(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(4, 'diamonds', '4_of_spades'), (4, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (0, 1, 2))

    def test_comparing_better_pair(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player2, 1, 1))

    def test_comparing_three_of_a_kind(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (4, 'spades', '13_of_spades'), (
            4, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player, 3, 0))
    def test_comparing_straight_flush(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(8, 'spades', '8_of_spades'),]
        self.app.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player, 52, 0))
    def test_comparing_straight(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(8, 'clubs', '8_of_clubs'),]
        self.app.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player, 4, 0))

    def test_comparing_flush(self):
        self.app.player.hand = [(4, 'spades', '4_of_spades'), (5, 'spades', '5_of_spades'), (6, 'spades', '6_of_spades'),
        (7, 'spades', '7_of_spades'),(9, 'spades', '9_of_spades'),]
        self.app.player2.hand = [(5, 'diamonds', '4_of_spades'), (2, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        self.app.player3.hand = [(4, 'diamonds', '4_of_spades'), (13, 'diamonds', '13_of_spades'), (
            5, 'diamonds', '5_of_clubs'), (8, 'diamonds', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        hv1 = self.app.player.hand_value()
        hv2 = self.app.player2.hand_value()
        hv3 = self.app.player3.hand_value()
        self.assertEqual(TestApp.compare(self, hv1, hv2, hv3), (self.app.player, 5, 0))
    def compare(self, hand_value1, hand_value2, hand_value3):
        hands = []
        hands.append((self.app.player, hand_value1))
        hands.append((self.app.player2, hand_value2))
        hands.append((self.app.player3, hand_value3))
        return self.app.compare_hands(hands)
