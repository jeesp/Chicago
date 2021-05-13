
import os 
import sys
import random
import pygame
from ui.menu_ui import start_menu, end_menu
from ui.gameplay_ui import draw_window, get_player_cards
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

class GUI:
    """
    Luokka graafiselle käyttöliittymälle. Konstruktorissa alustetaan pelitila
    ja graafiseen ilmeeseen liittyvät asiat.
    """
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Chicago')
        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 15
        self.current_path = os.path.dirname(__file__)
        self.CARD_SIZE = (80, 120)
        self.CARD_IMAGE = pygame.image.load(os.path.join(os.path.dirname(self.current_path),
                                                         'assets', 'cards', 'back-side.png'))
        self.CARD = pygame.transform.scale(self.CARD_IMAGE, self.CARD_SIZE)
        self.SIDE_CARD = pygame.transform.rotate(self.CARD, 90)
        self.POKER_GREEN = (53, 101, 77)
        self.mode = 0
        self.font = pygame.font.Font(None, 25)
        self.card_selected = False
        self.game_to_play = 0
    def main(self, app):
        """
        Päämetodi koko sovelluksen graafisen käyttöliittymän pyörittämiselle.
        """
        clock = pygame.time.Clock()
        players_cards = []
        continue_button = 0
        blanco_button = 0
        chicago_button = 0
        run = True
        random.shuffle(app.deck.cards)
        app.deck.deal_cards(app.players)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if self.game_to_play == 1:
                    app.play_poker(event, players_cards, continue_button, blanco_button)
                if self.game_to_play == 2:
                    app.play_trick(event, players_cards, continue_button, chicago_button)
            if self.mode == 0:
                button = start_menu(self, app)
                start_button = button[0]
                reset_button = button[1]
                app.menu_actions(event, start_button, reset_button)
            if self.mode == 1:
                draw_window(self, app)
                players_cards = get_player_cards(self, app, app.players[app.turn])
                continue_button = players_cards[1]
                blanco_button = players_cards[2]
                chicago_button = players_cards[3]
                players_cards = players_cards[0]
            if self.mode == 2:
                button = end_menu(self, app)
                start_button = button[0]
                reset_button = button[1]
                app.menu_actions(event, start_button, reset_button)
        pygame.quit()
        