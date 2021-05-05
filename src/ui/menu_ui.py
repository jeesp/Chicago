import pygame
from ui.gameplay_ui import print_scoreboard, print_text_lines
"""
Metodi luo alkuvalikon, josta saa aloitettua pelin.
"""
def start_menu(self):
    menu_object = create_menu_button(self, "Aloita")
    self.screen.blit(menu_object[1], menu_object[3])
    pygame.display.flip()
    return menu_object[2]
"""
Metodi luo loppuvalikon, josta saa aloitettua uuden pelin.
"""
def end_menu(self):
    menu_object = create_menu_button(self, "Uusi peli")
    newspace = 100
    for winningtext in self.winningtext:
        winning_text_line = menu_object[0].render(winningtext, True, (255, 255, 255))
        newline_rect = winning_text_line.get_rect(center=(menu_object[2].center))
        newline_rect.y += newspace
        newspace += 20
        self.screen.blit(winning_text_line, newline_rect)
    print_scoreboard(self)
    pygame.display.update()
    return menu_object[2]
"""
Metodi luo napin keskelle näyttöä halutulla tekstillä.
"""
def create_menu_button(self, button_text):
    self.screen.fill(self.POKER_GREEN, (0, 0, 800, 600))
    text = self.font.render(button_text, True, (255, 255, 255))
    button_width = 100
    button_height = 50
    new_game_button = pygame.Rect(self.WIDTH/2, self.HEIGHT/2, button_width, button_height)
    new_game_button.center = (self.WIDTH/2, self.HEIGHT/2)
    text_rect = text.get_rect(center=(new_game_button.center))
    color = (0,0,0)
    mouse_position = pygame.mouse.get_pos()
    if new_game_button.collidepoint(mouse_position):
        color = (50, 50, 50)
    pygame.draw.rect(self.screen, color, new_game_button)
    self.screen.blit(text, text_rect)
    pygame.display.flip()
    return (self.font, text, new_game_button, text_rect)