import os
import time
import pygame


def draw_window(self, app):
    """
    Metodi peli-ikkunan piirtämiseen.
    """
    self.screen.fill(self.POKER_GREEN, (0, 0, 800, 600))
    stack_height = 7
    deck_width = round(self.WIDTH/2 -self.CARD_SIZE[0]/2 -stack_height)
    deck_height = round(self.HEIGHT/2 -self.CARD_SIZE[1]/2 -stack_height)
    for i in range(stack_height):
        self.screen.blit(self.CARD, (deck_width, deck_height))
        deck_width += 2
        deck_height += 2
    space_between = 30
    left_player_width = 5
    left_player_height = round(self.HEIGHT/2 - self.CARD_SIZE[0] - space_between)
    right_player_width = self.WIDTH - self.CARD_SIZE[1] - left_player_width
    right_player_height = left_player_height
    top_player_width = round(self.WIDTH/2 - self.CARD_SIZE[0] -10)
    top_player_height = 5
    left_player = get_player_seat(app, app.turn)
    top_player = get_player_seat(app, left_player)
    right_player = get_player_seat(app, top_player)
    draw_other_player_cards(self, app, left_player, self.SIDE_CARD,
                            left_player_width, left_player_height, 1)
    draw_other_player_cards(self, app, top_player, self.CARD, 
                            top_player_width, top_player_height, 2)
    draw_other_player_cards(self, app, right_player, self.SIDE_CARD, 
                            right_player_width, right_player_height, 1)


def draw_other_player_cards(self, app, player, image, width, height, number):
    """
    Metodi piirtää näytölle toisten pelaajien kortit.
    """
    player_text = self.font.render(app.players[player].name, True, (255, 255, 255))
    if number == 1:
        player_text_rect = player_text.get_rect(center=(width + self.CARD_SIZE[1]/2, height - 20))
    if number == 2:
        player_text_rect = player_text.get_rect(center=(self.WIDTH/2, 150))
    space_between = 30
    for i in range(len(app.players[player].hand)):
        self.screen.blit(image, (width, height))
        if image == self.SIDE_CARD:
            height += space_between
        else:
            width += space_between
    self.screen.blit(player_text, player_text_rect)
def get_player_seat(app, previous):
    """
    Metodi hakee pelaajan pelipaikan.
    """
    new_player = previous + 1
    if new_player == len(app.players):
        new_player = 0
    return new_player
def print_scoreboard(self, app):
    """
    Metodi tulostaulun printtaamiselle.
    """
    height = 20
    width = 730
    score_text = self.font.render("Pisteet:", True, (255, 255, 255))
    score_text_rect = score_text.get_rect(center=(width, height))
    height += 20
    self.screen.blit(score_text, score_text_rect)
    for player in app.scoreboard:
        score_text = self.font.render(player.name + ": " + str(app.scoreboard[player]),
                                      True, (255, 255, 255))
        score_text_rect = score_text.get_rect(center=(width, height))
        height += 20
        self.screen.blit(score_text, score_text_rect)
def get_player_cards(self, app, player):
    """
    Metodi vuorossaolevan pelaajan korttien piirtämiseen, sekä pelitilanteiden printtaamiseen.
    """
    print_scoreboard(self, app)
    turn_text = self.font.render("Vuorossa " + app.players[app.turn].name, True, (255, 255, 255))
    turn_text_rect = turn_text.get_rect(center=(self.WIDTH/2, self.HEIGHT/2+100))
    self.screen.blit(turn_text, turn_text_rect)
    if self.game_to_play == 1:
        print_text_lines(self, app.poker_hand_lines, 150, 20)
    players_cards_as_rects = draw_player_cards(self, player)
    blanco_button = 0
    chicago_button = 0
    if app.deals == 1:
        blanco_button = draw_chicago_text(self, app, "Blanco huudettu! Blancon huusi ",
                                          blanco_button)
    chicago_check = app.check_chicago()
    if self.game_to_play == 2 and chicago_check[0]:
        chicago_button = draw_chicago_text(self, app, "Chicago huudettu! Chciagon huusi ",
                                           chicago_button)
    elif self.game_to_play == 2 and not chicago_check[0]:
        print_chicago_text(self, app, chicago_check)
    if self.game_to_play == 2:
        print_trick_compare_text(self, app)
    if app.blanco_is_on and self.game_to_play == 1:
        print_text_top_middle(self, "Valitse vähintään yksi kortti blancoa varten.")
    continue_button = draw_continue_button(self)
    pygame.display.update()
    blanco_object = [blanco_button, False]
    chicago_object = [chicago_button, False]
    return players_cards_as_rects, continue_button, blanco_object, chicago_object
def draw_player_cards(self, player):
    """
    Metodi piirtää näytölle vuorossaolevan pelaajan kortit.
    """
    players_cards_as_rects = []
    space_between = 20
    player_card_width = round(self.WIDTH/2 - (2*self.CARD_SIZE[0]
                                              + self.CARD_SIZE[0]/2 + 2*space_between))
    player_card_height = self.HEIGHT - self.CARD_SIZE[1] - 5
    for card in player.hand:
        PLAYER_CARD_IMAGE = pygame.image.load(os.path.join
                                              (os.path.dirname(self.current_path),
                                               'assets', 'cards', card[2] + '.png'))
        PLAYER_CARD = pygame.transform.scale(PLAYER_CARD_IMAGE, self.CARD_SIZE)
        card_rect = PLAYER_CARD.get_rect()
        card_rect.x = player_card_width
        card_rect.y = player_card_height
        self.screen.blit(PLAYER_CARD, card_rect)
        players_cards_as_rects.append([card, card_rect, PLAYER_CARD, False])
        player_card_width += self.CARD_SIZE[0] + space_between
    return players_cards_as_rects
def print_chicago_text(self, app, chicago_check):
    """
    Metodi chicago-tekstin luomiselle.
    """
    text_for_chicago = "Chicago huudettu! Chicagon huusi "
    if chicago_check[2]:
        text_for_chicago = "Blanco huudettu! Blancon huusi "
    chicago_check = app.check_chicago()
    chicago_player = chicago_check[1]
    print_text_top_middle(self, text_for_chicago + chicago_player.name)

def print_text_top_middle(self, text):
    text_object = self.font.render(text, True, (255, 255, 255))
    text_rect = text_object.get_rect(center=(self.WIDTH/2, self.HEIGHT/2-100))
    self.screen.blit(text_object, text_rect)
def print_trick_compare_text(self, app):
    """
    Metodi piirtää näytölle tekstin pelatusta chicago-kortista.
    """
    if app.compare_card is not None:
        if app.compare_card[1] == 'hearts':
            maa = 'hertta'
        if app.compare_card[1] == 'clubs':
            maa = 'risti'
        if app.compare_card[1] == 'spades':
            maa = 'pata'
        if app.compare_card[1] == 'diamonds':
            maa = 'ruutu'
        lines = []
        line = "Pelattu kortti: " + maa + ", " + str(app.compare_card[0])
        line2 = " Kortin pelasi: " + app.compare_card[2].name
        lines.append(line)
        lines.append(line2)
        print_text_lines(self, lines, self.WIDTH/2, self.HEIGHT/2+120)
def draw_chicago_text(self, app, text, button):
    """
    Metodi chicago-tekstin piirtämiseen näytölle.
    """
    chicago_check = app.check_chicago()
    chicago_player = chicago_check[1]
    black = (0, 0, 0)
    if chicago_check[0]:
        if app.deals == 1:
            button = draw_blanco_button(self, black)
        if self.game_to_play == 2 and chicago_check[0] and len(app.players[app.turn].hand) > 4:
            button = draw_chicago_button(self, black)
    else:
        print_text_top_middle(self, text + chicago_player.name)
    return button
def draw_continue_button(self):
    """
    Metodi "Jatka"-painikkeen luomiseen.
    """
    color = (0, 0, 0)
    continue_text = self.font.render('Jatka', True, (255,255,255))
    continue_button = pygame.Rect(680, 510, 100, 50)
    mouse_position = pygame.mouse.get_pos()
    if continue_button.collidepoint(mouse_position):
        color = (50, 50, 50)
    pygame.draw.rect(self.screen, color, continue_button)
    continue_text_rect = continue_text.get_rect(center=(continue_button.center))
    self.screen.blit(continue_text, continue_text_rect)
    return continue_button
def draw_blanco_button(self, color):
    """
    Metodi Blanco-painikkeen luomiseen.
    """
    blanco_button = draw_coloured_button(self, color, 'Blanco')
    return blanco_button
def draw_chicago_button(self, color):
    """
    Metodi Chicago-painikkeen luomiseen.
    """
    chicago_button = draw_coloured_button(self, color, 'Chicago')
    return chicago_button
def draw_coloured_button(self, color, text):
    """
    Metodi värillisen Chicago/Blanco-painikkeen luomiseen.
    """
    text = self.font.render(text, True, (255, 255, 255))
    button = pygame.Rect(20, 510, 100, 50)
    mouse_position = pygame.mouse.get_pos()
    if button.collidepoint(mouse_position):
        if color == (0, 0, 0):
            color = (50, 50, 50)
        elif color == (0, 200, 0):
            color = (0, 150, 0)
    pygame.draw.rect(self.screen, color, button)
    text_rect = text.get_rect(center=(button.center))
    self.screen.blit(text, text_rect)
    return button
def trick_card_select(self, app, players_cards):
    """
    Metodi tikin kortinvalinnalle.
    """
    mouse_position = pygame.mouse.get_pos()
    not_same_suits = True
    if app.compare_card is not None:
        for card in players_cards:
            if card[0][1] is app.compare_card[1]:
                not_same_suits = False
    for card in players_cards:
        if card[1].collidepoint(mouse_position):
            if app.compare_card is None or card[0][1] is app.compare_card[1] or not_same_suits:
                draw_green_on_card(self, card)
                x_change = 5
                y_change = 15
                if not card[3] and not self.card_selected:
                    lift_card_up(self, card, x_change, y_change)
                    self.card_selected = True
                elif card[3] and self.card_selected:
                    put_card_down(card, x_change, y_change)
                    self.card_selected = False
                update_card(self, card)
def poker_card_select(self, players_cards):
    """
    Metodi pokerin kortinvalinnalle.
    """
    mouse_position = pygame.mouse.get_pos()
    for card in players_cards:
        if card[1].collidepoint(mouse_position):
            draw_green_on_card(self, card)
            x_change = 5
            y_change = 15
            if not card[3]:
                lift_card_up(self, card, x_change, y_change)
            else:
                put_card_down(card, x_change, y_change)
            update_card(self, card)
def update_card(self, card):
    """
    Metodi päivittää kortin tilan näytölle.
    """
    self.screen.blit(card[2], card[1])
    pygame.display.update()
    self.mode = 3
def draw_green_on_card(self, card):
    """
    Metodi piirtää halutun kortin päälle taustavärillä.
    """
    pygame.draw.rect(self.screen,
                     self.POKER_GREEN,
                     pygame.Rect(card[1].x,
                                 card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
    pygame.display.flip()
def lift_card_up(self, card, x_change, y_change):
    """
    Metodi piirtää efektin kortinnostosta näytölle.
    """
    pygame.draw.rect(self.screen,
                     (25, 25, 25),
                     pygame.Rect(card[1].x,
                                 card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
    card[1].x += x_change
    card[1].y -= y_change
    card[3] = True
def put_card_down(card, x_change, y_change):
    """
    Metodi piirtää efektin kortin laskemisesta näytölle.
    """
    card[1].x -= x_change
    card[1].y += y_change
    card[3] = False
def print_round_ending_lines(self, app):
    """
    Metodi piirtää kierroksen lopetustekstit näytölle.
    """
    refresh_round_ending_lines(self, app, app.round_ending_lines)
    time.sleep(3)
    refresh_round_ending_lines(self, app, app.poker_hand_lines)
def refresh_round_ending_lines(self, app, lines):
    """
    Metodi päivittää kierroksen lopetusnäytön tekstit ja poistaa vanhat.
    """
    self.screen.fill(self.POKER_GREEN, (0, 0, 800, 600))
    print_scoreboard(self, app)
    print_text_lines(self, lines, self.WIDTH/2, self.HEIGHT/2)
    pygame.display.update()
def print_text_lines(self, lines, width, height):
    """
    Metodi piirtää halutut tekstit näytölle.
    """
    for line in lines:
        compare_card_text = self.font.render(line, True, (255, 255, 255))
        compare_card_text_rect = compare_card_text.get_rect(center=(width, height))
        self.screen.blit(compare_card_text, compare_card_text_rect)
        height += 20
def remove_played_cards(self, players_cards):
    """
    Metodi piirtää taustavärillä pelaajan korttien päälle.
    """
    played_cards = []
    for card in players_cards:
        if card[3]:
            played_cards.append(card[0])
        pygame.draw.rect(self.gui.screen, self.gui.POKER_GREEN,
                         pygame.Rect(card[1].x-20,
                                     card[1].y-20, self.gui.CARD_SIZE[0]+20,
                                     self.gui.CARD_SIZE[1]+40))
    pygame.display.update()
    return played_cards
