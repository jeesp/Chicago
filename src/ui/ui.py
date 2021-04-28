import pygame
import os, sys
import time
import random
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from entities.player import Player
from entities.deck import Deck
from game_actions import play_poker, play_trick, compare_hands, round_ending, poker_points

class GUI(object):
    def __init__(self):
        players = []
        player1 = Player('Ake')
        players.append(player1)
        player2 = Player('Make')
        players.append(player2)
        player3 = Player('Jake')
        players.append(player3)
        player4 = Player('Åke')
        players.append(player4)
        self.score_board = dict()
        for player in players:
            self.score_board[player] = 0
        self.hand_values = {0: "Ei mitään", 1: "Pari", 2: "Kaksi paria", 3: "Kolmoset", 4: "Suora",
                       5: "Väri", 6: "Täyskäsi", 8: "Neloset", 10: "Värisuora"}
        self.deals = 0
        self.dealing_turn = 0
        self.starting_player = 0
        deck = Deck()
        self.players = players
        self.deck = deck
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

    def draw_window(self):
        self.screen.fill(self.POKER_GREEN, (0,0, 800, 600))
        stack_height = 7
        deck_width = round(self.WIDTH/2 -self.CARD_SIZE[0]/2 -stack_height)
        deck_height = round(self.HEIGHT/2 -self.CARD_SIZE[1]/2 -stack_height)
        for x in range(stack_height):
            self.screen.blit(self.CARD, (deck_width,deck_height))
            deck_width += 2
            deck_height += 2
        space_between = 30
        left_player_width = 5
        left_player_height = round(self.HEIGHT/2 - self.CARD_SIZE[0] - space_between)
        right_player_width = self.WIDTH - self.CARD_SIZE[1] - left_player_width
        right_player_height = left_player_height
        top_player_width = round(self.WIDTH/2 - self.CARD_SIZE[0] -space_between)
        top_player_height = 5
        space_between = 30
        for i in range(5):
            self.screen.blit(self.SIDE_CARD, (left_player_width,left_player_height))
            self.screen.blit(self.SIDE_CARD, (right_player_width,right_player_height))
            self.screen.blit(self.CARD, (top_player_width, top_player_height))
            left_player_height += space_between
            right_player_height += space_between
            top_player_width += space_between
    def get_player_cards(self, player):
        players_cards_as_rects = []
        space_between = 20
        player_card_width = round(self.WIDTH/2 - (2*self.CARD_SIZE[0] + self.CARD_SIZE[0]/2 + 2*space_between))
        player_card_height = self.HEIGHT - self.CARD_SIZE[1] - 5
        for card in player.hand:
            PLAYER_CARD_IMAGE = pygame.image.load(os.path.join(os.path.dirname(self.current_path),'assets', 'cards', card[2] + '.png'))
            PLAYER_CARD = pygame.transform.scale(PLAYER_CARD_IMAGE, self.CARD_SIZE)
            card_rect = PLAYER_CARD.get_rect()
            card_rect.x = player_card_width
            card_rect.y = player_card_height
            self.screen.blit(PLAYER_CARD, card_rect)
            players_cards_as_rects.append([card, card_rect, PLAYER_CARD, False])
            player_card_width += self.CARD_SIZE[0] + space_between
        font = pygame.font.SysFont('Ariel', 35)
        text = font.render('Jatka', True, (255,255,255))
        continue_button = pygame.Rect(680, 510, 100, 50)
        pygame.draw.rect(self.screen, (0,0,0), continue_button)
        self.screen.blit(text, (695,525))
        pygame.display.update()
        return players_cards_as_rects, continue_button
    def main_menu(self):
        self.screen.fill(self.POKER_GREEN, (0,0, 800, 600))
        font_size = 35
        font = pygame.font.SysFont('Ariel', font_size)
        text = font.render('Aloita', True, (255,255,255))
        button_width = 100
        button_height = 50
        start_width = round(self.WIDTH/2-button_width/2)
        start_height = round(self.HEIGHT/2-button_height/2)
        start_button = pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(start_width, start_height, button_width, button_height))
        self.screen.blit(text, (start_width+15,start_height+15))
        pygame.display.update()
        return start_button
    def main(self):
        clock = pygame.time.Clock()
        players_cards = []
        continue_button = pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(0,0, self.CARD_SIZE[0], self.CARD_SIZE[1]))
        run = True
        self.game_to_play = 0
        random.shuffle(self.deck.cards)
        self.deck.deal_cards(self.players)
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if self.deals == 2:
                    self.game_to_play = 2
                    self.turn = self.start
                    self.deals = 3
                    hands = []
                    for player in self.players:
                        hand = player.hand_value()
                        hands.append((player, hand))
                    self.value_comparison = compare_hands(hands)
                if self.game_to_play == 1:
                    play_poker(self, event, players_cards, continue_button)
                if self.game_to_play == 2:
                    play_trick(self, event, players_cards, continue_button)
            if self.mode == 0:
                start_button = self.main_menu()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_position = pygame.mouse.get_pos()
                    if start_button.collidepoint(mouse_position):
                        self.mode = 1
                        self.game_to_play = 1
                        random.shuffle(self.deck.cards)
                        self.deck.deal_cards(self.players)
                        chicago = dict()
                        for player in self.players:
                            chicago[player] = 0
                        poker_points(self)
            if self.mode == 1:
                self.draw_window()
                players_cards = self.get_player_cards(self.players[self.turn])
                continue_button = players_cards[1]
                players_cards = players_cards[0]
        pygame.quit()
    
if __name__ == "__main__":
    gui = GUI()
    gui.main()
        