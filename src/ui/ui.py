
import os 
import sys
import random
import pygame
from ui.menu_ui import start_menu, end_menu
from ui.gameplay_ui import draw_window, get_player_cards, draw_continue_button
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from entities.deck import Deck
from game_logic.game_actions import play_poker, play_trick, set_up_players, set_up_scoreboard
from game_logic.game_actions import set_up_chicago, menu_actions, add_players
from repository.highscore_repository import HighscoreRepository
from database_connection import get_database_connection

"""
Luokka graafiselle käyttöliittymälle, kaikki toiminnallisuudet perustuvat tämän luokan muuttujiin.
"""
class GUI(object):
    def __init__(self):
        self.highscore_repository = HighscoreRepository(get_database_connection())
        add_players(self, ["Pelaaja 1", "Pelaaja 2", "Pelaaja 3", "Pelaaja 4"])
        self.players = []
        set_up_players(self)
        self.scoreboard = dict()
        set_up_scoreboard(self)
        self.chicago = dict()
        set_up_chicago(self)
        self.hand_values = {0: "Ei mitään", 1: "Pari", 2: "Kaksi paria", 3: "Kolmoset", 4: "Suora",
                       5: "Väri", 6: "Täyskäsi", 8: "Neloset", 10: "Värisuora"}
        self.deals = 0
        self.dealing_turn = 0
        self.starting_player = 0
        self.deck = Deck()
        pygame.init()
        pygame.display.set_caption('Chicago')
        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 15
        self.current_path = os.path.dirname(__file__)
        self.CARD_SIZE = (80, 120)
        self.CARD_IMAGE = pygame.image.load(os.path.join(os.path.dirname(self.current_path), 'assets', 'cards', 'back-side.png'))
        self.CARD = pygame.transform.scale(self.CARD_IMAGE, self.CARD_SIZE)
        self.SIDE_CARD = pygame.transform.rotate(self.CARD, 90)
        self.POKER_GREEN = (53, 101, 77)
        self.mode = 0
        self.turn = 0
        self.card_selected = False
        self.played_cards = []
        self.compare_card = None
        self.start = 0
        self.value_comparison = (0, 0, 0)
        self.winningtext = []
        self.chicago_on = False
        self.chicago_successful = False
        self.chicago_player = None
        self.blanco_is_on = False
        self.font = pygame.font.Font(None, 25)
        self.poker_hand_lines = []
        self.round_ending_lines = []
        self.points_reseted = False
    """
    Päämetodi koko sovelluksen graafisen käyttöliittymän pyörittämiselle.
    """
    def main(self):
        clock = pygame.time.Clock()
        players_cards = []
        continue_button = 0
        blanco_button = 0
        chicago_button = 0
        run = True
        self.game_to_play = 0
        random.shuffle(self.deck.cards)
        self.deck.deal_cards(self.players)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if self.game_to_play == 1:
                    play_poker(self, event, players_cards, continue_button, blanco_button)
                if self.game_to_play == 2:
                    play_trick(self, event, players_cards, continue_button, chicago_button)
            if self.mode == 0:
                button = start_menu(self)
                menu_actions(self, event, button)
            if self.mode == 1:
                draw_window(self)
                players_cards = get_player_cards(self, self.players[self.turn])
                continue_button = players_cards[1]
                blanco_button = players_cards[2]
                chicago_button = players_cards[3]
                players_cards = players_cards[0]
            if self.mode == 2:
                button = end_menu(self)
                menu_actions(self, event, button)
        pygame.quit()
        