import pygame
from ui.gameplay_ui import print_scoreboard

def start_menu(self, app):
    """
    Metodi luo alkuvalikon, josta saa aloitettua pelin.
    """
    self.screen.fill(self.POKER_GREEN, (0, 0, 800, 600))
    menu_object = create_menu_button(self, "Aloita", self.WIDTH/2, self.HEIGHT/2)
    self.screen.blit(menu_object[1], menu_object[3])
    reset_button = print_highscore_table(self, app)
    pygame.display.update()
    return (menu_object[2], reset_button)
def get_points(app):
    """
    Metodi pisteidenhaulle tietokannasta.
    """
    names = app.highscore_repository.get_players()
    pointlist = []
    for name in names:
        points = app.highscore_repository.get_points(name)
        pointlist.append((name, points))
    return pointlist
def print_highscore_table(self, app):
    """
    Metodi piirtää näytölle tietokannasta haettavan kokonaispisteiden tulostaulun.
    """
    height = 20
    width = 100
    score_text = self.font.render("Kokonaispisteet:", True, (255, 255, 255))
    score_text_rect = score_text.get_rect(center=(width, height))
    height += 20
    self.screen.blit(score_text, score_text_rect)
    points = get_points(app)
    for player in points:
        score_text = self.font.render(player[0] + ": " + str(player[1]), True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(width, height))
        height += 20
        self.screen.blit(score_text, score_text_rect)
    height += 30
    highscore_button = create_menu_button(self, "Nollaa", width, height)
    return highscore_button[2]
def end_menu(self, app):
    """
    Metodi luo loppuvalikon, josta saa aloitettua uuden pelin.
    """
    self.screen.fill(self.POKER_GREEN, (0, 0, 800, 600))
    menu_object = create_menu_button(self, "Uusi peli", self.WIDTH/2, self.HEIGHT/2)
    newspace = 100
    for winningtext in app.winningtext:
        winning_text_line = menu_object[0].render(winningtext, True, (255, 255, 255))
        newline_rect = winning_text_line.get_rect(center=(menu_object[2].center))
        newline_rect.y += newspace
        newspace += 20
        self.screen.blit(winning_text_line, newline_rect)
    reset_button = print_highscore_table(self, app)
    print_scoreboard(self, app)
    pygame.display.update()
    return (menu_object[2], reset_button)
def create_menu_button(self, button_text, width, height):
    """
    Metodi luo napin näytölle halutulla tekstillä.
    """
    text = self.font.render(button_text, True, (255, 255, 255))
    button_width = 100
    button_height = 50
    new_game_button = pygame.Rect(width, height, button_width, button_height)
    new_game_button.center = (width, height)
    text_rect = text.get_rect(center=(new_game_button.center))
    color = (0, 0, 0)
    mouse_position = pygame.mouse.get_pos()
    if new_game_button.collidepoint(mouse_position):
        color = (50, 50, 50)
    pygame.draw.rect(self.screen, color, new_game_button)
    self.screen.blit(text, text_rect)
    return (self.font, text, new_game_button, text_rect)
