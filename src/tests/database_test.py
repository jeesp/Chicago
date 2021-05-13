import unittest
from game_logic.game_actions import App
class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.highscore_repository.delete_all()
        self.app.set_up_players()
    def test_get_game_id(self):
        self.assertEqual(self.app.highscore_repository.get_latest_game(), 1)
    def test_get_players(self):
        self.assertEqual(len(self.app.highscore_repository.get_players()), 4)
    def test_get_player_id(self):
        self.assertEqual(self.app.highscore_repository.get_player_id("Pelaaja 1"), 1)
    def test_get_points(self):
        self.assertEqual(self.app.highscore_repository.get_points("Pelaaja 1"), 0)
    def test_add_name(self):
        self.app.highscore_repository.add_name("Pelaaja 5")
        self.assertEqual(len(self.app.highscore_repository.get_players()), 5)
    def test_add_new_game(self):
        game_objects = []
        game_objects.append([1, 1, 52])
        self.app.highscore_repository.add_new_game(game_objects)
        self.assertEqual(self.app.highscore_repository.get_latest_game(), 2)
        self.assertEqual(self.app.highscore_repository.get_points("Pelaaja 1"), 52)
    #def test_create_game_object(self):
    #    print(self.app.highscore_repository.get_players())
    #    self.app.highscore_repository.create_game_object(self.app)
    #    self.assertEqual(self.app.highscore_repository.get_latest_game(), 1)
