import pygame
import os
import time

class GUI():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Chicago')
        self.WIDTH = 800
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.FPS = 60
        self.current_path = os.path.dirname(__file__)
        self.CARD_SIZE = (80,120)
        self.CARD_IMAGE = pygame.image.load(os.path.join(self.current_path,'assets', 'cards', 'back-side.png'))
        self.CARD = pygame.transform.scale(self.CARD_IMAGE, self.CARD_SIZE)
        self.SIDE_CARD = pygame.transform.rotate(self.CARD, 90)
        self.POKER_GREEN = (53,101,77)

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
        for card in player[1]:
            PLAYER_CARD_IMAGE = pygame.image.load(os.path.join(self.current_path,'assets', 'cards', card[2] + '.png'))
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
        self.screen.blit(text, (695,520))
        pygame.display.update()
        return players_cards_as_rects, continue_button
    def main_menu(self):
        self.screen.fill(self.POKER_GREEN, (0,0, 800, 600))
    def main(self):

        cards = [(4, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
                5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
        cards2 = [(6, 'spades', '6_of_spades'), (2, 'spades', '2_of_spades'), (
                12, 'clubs', 'queen_of_clubs'), (4, 'spades', '4_of_spades'), (7, 'hearts', '7_of_hearts')]
        clock = pygame.time.Clock()
        player1 = ("Masa", cards)
        player2 = ("Kake", cards2)
        players = []
        players.append(player1)
        players.append(player2)
        turn = 0
        players_cards = []
        continue_button = pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(0,0, self.CARD_SIZE[0], self.CARD_SIZE[1]))
        run = True
        mode = 1
        while run:
            clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_position = pygame.mouse.get_pos()
                    for card in players_cards:
                        if card[1].collidepoint(mouse_position):
                            pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x, card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                            pygame.display.flip()
                            if card[3] == False:
                                pygame.draw.rect(self.screen, (25,25,25), pygame.Rect(card[1].x, card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                                x_change = 5
                                y_change = 15
                                card[1].x += x_change
                                card[1].y -= y_change
                                card[3] = True
                            else:
                                card[1].x -= x_change
                                card[1].y += y_change
                                card[3] = False
                            self.screen.blit(card[2], card[1])
                            pygame.display.update()
                            mode = 2
                            print(card)
                    if continue_button.collidepoint(mouse_position):
                        cards_clicked = []
                        for card in players_cards:
                            if card[3]:
                                cards_clicked.append(card[0])
                            pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x-20, card[1].y-20, self.CARD_SIZE[0]+20, self.CARD_SIZE[1]+40))
                        pygame.display.update()
                        time.sleep(1)

                        print("ok")
                        turn += 1
                        if turn == len(players):
                            turn = 0
                        mode= 1

            if mode == 0:
                self.main_menu()
            if mode == 1:
                self.draw_window()
                players_cards = self.get_player_cards(players[turn])
                continue_button = players_cards[1]
                players_cards = players_cards[0]

        pygame.quit()

if __name__ == "__main__":
    guivariable = GUI()
    guivariable.main()
        