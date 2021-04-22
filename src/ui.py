import pygame
import os

pygame.init()
pygame.display.set_caption('Chicago')
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
current_path = os.path.dirname(__file__)
CARD_SIZE = (80,120)
CARD_IMAGE = pygame.image.load(os.path.join(current_path,'assets', 'cards', 'back-side.png'))
CARD = pygame.transform.scale(CARD_IMAGE, CARD_SIZE)
SIDE_CARD = pygame.transform.rotate(CARD, 90)
POKER_GREEN = (53,101,77)
def draw_window():
    screen.fill(POKER_GREEN, (0,0, 800, 600))
    stack_height = 7
    deck_width = round(WIDTH/2 -CARD_SIZE[0]/2 -stack_height)
    deck_height = round(HEIGHT/2 -CARD_SIZE[1]/2 -stack_height)
    for x in range(stack_height):
        screen.blit(CARD, (deck_width,deck_height))
        deck_width += 2
        deck_height += 2
    space_between = 30
    left_player_width = 5
    left_player_height = round(HEIGHT/2 - CARD_SIZE[0] - space_between)
    right_player_width = WIDTH - CARD_SIZE[1] - left_player_width
    right_player_height = left_player_height
    top_player_width = round(WIDTH/2 - CARD_SIZE[0] -space_between)
    top_player_height = 5
    space_between = 30
    for i in range(5):
        screen.blit(SIDE_CARD, (left_player_width,left_player_height))
        screen.blit(SIDE_CARD, (right_player_width,right_player_height))
        screen.blit(CARD, (top_player_width, top_player_height))
        left_player_height += space_between
        right_player_height += space_between
        top_player_width += space_between
def get_player_cards(player):
    players_cards_as_rects = []
    space_between = 20
    player_card_width = round(WIDTH/2 - (2*CARD_SIZE[0] + CARD_SIZE[0]/2 + 2*space_between))
    player_card_height = HEIGHT - CARD_SIZE[1] - 5
    for card in player[1]:
        PLAYER_CARD_IMAGE = pygame.image.load(os.path.join(current_path,'assets', 'cards', card[2] + '.png'))
        PLAYER_CARD = pygame.transform.scale(PLAYER_CARD_IMAGE, CARD_SIZE)
        card_rect = PLAYER_CARD.get_rect()
        card_rect.x = player_card_width
        card_rect.y = player_card_height
        screen.blit(PLAYER_CARD, card_rect)
        players_cards_as_rects.append([card, card_rect, PLAYER_CARD, True])
        player_card_width += CARD_SIZE[0] + space_between
    pygame.display.update()
    return players_cards_as_rects
def main_menu():
    screen.fill(POKER_GREEN, (0,0, 800, 600))
def main():
    
    cards = [(4, 'spades', '4_of_spades'), (13, 'spades', 'king_of_spades'), (
            5, 'clubs', '5_of_clubs'), (8, 'spades', '8_of_spades'), (3, 'hearts', '3_of_hearts')]
    clock = pygame.time.Clock()
    player1 = ("Masa", cards)
    players = []
    players.append(player1)
    turn = 0
    players_cards = []
    run = True
    mode = 1
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_position = pygame.mouse.get_pos()
                for card in players_cards:
                    if card[1].collidepoint(mouse_position):
                        pygame.draw.rect(screen, POKER_GREEN, pygame.Rect(card[1].x, card[1].y, CARD_SIZE[0], CARD_SIZE[1]))
                        pygame.display.flip()
                        if card[3]:
                            pygame.draw.rect(screen, (50,50,50), pygame.Rect(card[1].x, card[1].y, CARD_SIZE[0], CARD_SIZE[1]))
                            x_change = 2
                            y_change = 6
                            card[1].x += x_change
                            card[1].y -= y_change
                            card[3] = False
                        else:
                            card[1].x -= x_change
                            card[1].y += y_change
                            card[3] = True
                        screen.blit(card[2], card[1])
                        pygame.display.update()
                        mode = 2
                        print(card)
        if mode == 0:
            main_menu()
        if mode == 1:
            draw_window()
            players_cards = get_player_cards(players[turn])

    pygame.quit()

if __name__ == "__main__":
    main()