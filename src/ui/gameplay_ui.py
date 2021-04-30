import pygame
import os
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