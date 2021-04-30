import pygame
import os, sys
import time
import random
from menu_ui import start_menu, end_menu, create_menu_button
from gameplay_ui import draw_window, get_player_cards
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from entities.player import Player
from entities.deck import Deck
from game_actions import play_poker, play_trick, compare_hands, round_ending, poker_points, set_up_players, set_up_scoreboard, menu_actions


class GUI(object):
    def __init__(self):
        set_up_players(self)
        set_up_scoreboard(self)
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
        self.CARD_SIZE = (80,120)
        self.CARD_IMAGE = pygame.image.load(os.path.join(os.path.dirname(self.current_path),'assets', 'cards', 'back-side.png'))
        self.CARD = pygame.transform.scale(self.CARD_IMAGE, self.CARD_SIZE)
        self.SIDE_CARD = pygame.transform.rotate(self.CARD, 90)
        self.POKER_GREEN = (53,101,77)
        self.mode = 0
        self.turn = 0
        self.card_selected = False
        self.played_cards = []
        self.compare_card = None
        self.start = 0
        self.value_comparison = (0,0)
        self.winningtext = []

    
    def main(self):
        clock = pygame.time.Clock()
        players_cards = []
        continue_button = 0
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
                    play_poker(self, event, players_cards, continue_button)
                if self.game_to_play == 2:
                    play_trick(self, event, players_cards, continue_button)
            if self.mode == 0:
                button = start_menu(self)
                menu_actions(self, event, button)
            if self.mode == 1:
                draw_window(self)
                players_cards = get_player_cards(self, self.players[self.turn])
                continue_button = players_cards[1]
                players_cards = players_cards[0]
            if self.mode == 2:
                button = end_menu(self)
                menu_actions(self, event, button)
        pygame.quit()
    
if __name__ == "__main__":
    gui = GUI()
    gui.main()
        