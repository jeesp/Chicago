import time
import random
import pygame
from entities.deck import Deck
from entities.player import Player
from ui.gameplay_ui import draw_blanco_button, draw_continue_button, draw_chicago_button
from ui.gameplay_ui import trick_card_select, poker_card_select, print_round_ending_lines
"""
Metodi palauttaa pokerikäden vertailun tuloksen.
"""
def end_game_poker_points(self):
    if self.value_comparison[0] != 0:
        self.scoreboard[self.value_comparison[0]] += self.value_comparison[1]
        if self.value_comparison[2] == 0:
            self.round_ending_lines.append("Lopun pokeripisteet sai: " 
                                           + self.value_comparison[0].name)
            self.round_ending_lines.append("Käsi: "
                                           + self.hand_values[self.value_comparison[1]].lower() + ".")
        if self.value_comparison[2] == 1:
            self.round_ending_lines.append("Lopun pokeripisteet sai: " 
                                           + self.value_comparison[0].name)
            self.round_ending_lines.append("Käsi: " + self.hand_values[self.value_comparison[1]].lower())
            self.round_ending_lines.append("Myös toisella pelaajalla oli "
                                           + self.hand_values[self.value_comparison[1]].lower() + ".")
        if self.value_comparison[1] == 8:
            if not self.points_reseted:
                self.points_reseted = True
                for player in self.scoreboard:
                    if player != self.value_comparison[0]:
                        self.scoreboard[player] == 0
                self.round_ending_lines.append("Pelaajien pisteet nollattiin nelosten takia.")
        if self.value_comparison[1] == 52:
            for player in self.scoreboard:
                if player != self.value_comparison[0]:
                    self.scoreboard[player] == 0
            self.round_ending_lines.append("Pelaajien pisteet värisuoran takia.")
    if self.value_comparison[2] == 2:
        self.round_ending_lines.append("Kahdella pelaajalla oli sama käsi: "
                                       + self.hand_values[self.value_comparison[1]].lower())
        self.round_ending_lines.append(". Kukaan ei saanut pisteitä.")
    if self.value_comparison[0] == 0:
        self.round_ending_lines.append("Kenelläkään ei ollut mitään, joten kukaan ei saanut lopun "
                                       + "pokeripisteitä.")
"""
Metodi luo pelaajat peliin.
"""
def set_up_players(self):
    self.players = []
    player1 = Player('Ake')
    self.players.append(player1)
    player2 = Player('Make')
    self.players.append(player2)
    player3 = Player('Jake')
    self.players.append(player3)
    player4 = Player('Åke')
    self.players.append(player4)
"""
Metodi luo tulostaulun.
"""
def set_up_scoreboard(self):
    self.scoreboard = dict()
    for player in self.players:
        self.scoreboard[player] = 0
"""
Metodi laskee ja vertaa pokerikäsien arvot sekä lisää voittajalle pisteet. 
Metodi myös palauttaa tulostettavat tekstit pokerikierrokselta.
"""
def set_up_chicago(self):
    self.chicago = dict()
    for player in self.players:
        self.chicago[player] = 0
    self.chicago_on = False
    self.chicago_successful = False
    self.chicago_player = None
    self.blanco_is_on = False
def poker_points(self):
    hands = []
    self.poker_hand_lines = []
    for player in self.players:
        hand = player.hand_value()
        hands.append((player, hand))
    self.value_comparison = compare_hands(hands)
    if self.value_comparison[0] != 0:
        self.scoreboard[self.value_comparison[0]] += self.value_comparison[1]
        if self.value_comparison[2] == 0:
            line = "Pisteet " + str(self.deals + 1) + ". kierrokselta sai: " + self.value_comparison[0].name
            self.poker_hand_lines.append(line)
            line = "Käsi: " + self.hand_values[self.value_comparison[1]].lower() + "."
            self.poker_hand_lines.append(line)
        if self.value_comparison[2] == 1:
            line = "Pisteet " + str(self.deals + 1) + ". kierrokselta sai: " + self.value_comparison[0].name
            self.poker_hand_lines.append(line)
            line = ("Käsi: " + self.hand_values[self.value_comparison[1]].lower())
            self.poker_hand_lines.append(line)
            line = ("Myös toisella pelaajalla oli "
                    + self.hand_values[self.value_comparison[1]].lower() + ".")
            self.poker_hand_lines.append(line)
        if self.value_comparison[1] == 8:
            if not self.points_reseted:
                self.points_reseted = True
                for player in self.scoreboard:
                    if player != self.value_comparison[0]:
                        self.scoreboard[player] == 0
                line = ("Pelaajien pisteet nollattiin nelosten takia.")
                self.poker_hand_lines.append(line)
        if self.value_comparison[1] == 52:
            for player in self.scoreboard:
                if player != self.value_comparison[0]:
                    self.scoreboard[player] == 0
            line = ("Pelaajien pisteet värisuoran takia.")
    elif self.value_comparison[2] == 2:
        line = ("Kahdella pelaajalla on sama käsi: "
                + self.hand_values[self.value_comparison[1]].lower() + ".")
        self.poker_hand_lines.append(line)
        line = "Kukaan ei saanut pisteitä."
        self.poker_hand_lines.append(line)
    else:
        self.poker_hand_lines.append("Kenelläkään ei ollut mitään, joten kukaan ei saanut pisteitä.")

"""
Metodi pokerikierroksen pelaamiseen ja graafisen käyttöliittymän päivittämiseen.
"""
def play_poker(self, event, players_cards, continue_button, blanco_object):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_position = pygame.mouse.get_pos()
        poker_card_select(self,players_cards)
        if blanco_object[0] != 0:
            if blanco_object[0].collidepoint(mouse_position):
                if not blanco_object[1]:
                    color = (0, 200, 0)
                    draw_blanco_button(self, color)
                    blanco_object[1] = True
                    print(blanco_object)
                else:
                    color = (0, 0, 0)
                    draw_blanco_button(self, color)
                    blanco_object[1] = False
                    print(blanco_object)
            pygame.display.update()
            self.mode = 3
        if continue_button.collidepoint(mouse_position):
            if blanco_object[1]:
                self.chicago[self.players[self.turn]] = 2
            cards_clicked = []
            print(self.chicago)
            pygame.display.flip()
            for card in players_cards:
                if card[3]:
                    cards_clicked.append(card[0])
                pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x-20,
                card[1].y-20, self.CARD_SIZE[0]+20, self.CARD_SIZE[1]+40))
            pygame.display.update()
            change_card(self, self.players[self.turn], cards_clicked)
            self.turn += 1
            if self.turn == len(self.players):
                self.turn = 0
            if self.turn == self.dealing_turn:
                random.shuffle(self.deck.cards)
                self.deck.deal_cards(self.players)
                self.deals += 1
                if self.deals < 2:
                    print(poker_points(self))
                if self.deals == 2:
                    self.game_to_play = 2
                    for player in self.chicago:
                        if self.chicago[player] != 0:
                            self.start = self.players.index(player)
                            self.game_to_play = 2
                            self.chicago_player = self.players[self.turn]
                            self.chicago_successful = True
                            self.chicago_on = True
                            self.blanco_is_on = True
                    self.turn = self.start
                    self.deals = 3
                    print(self.players[self.turn].name)
                    hands = []
                    for player in self.players:
                        hand = player.hand_value()
                        hands.append((player, hand))
                    self.value_comparison = compare_hands(hands)
            self.mode = 1
    draw_continue_button(self)
    if blanco_object[0] != 0:
        if blanco_object[1]:
            color = (0, 200, 0)
            draw_blanco_button(self, color)
        else:
            color = (0, 0, 0)
            draw_blanco_button(self, color)
    pygame.display.update()
"""
Metodi kortin vaihtoon.
"""
def change_card(self, player, cards_clicked):
    for card in cards_clicked:
        self.deck.add_card_to_dealt_cards(card)
        player.remove_card(card)
"""
Metodi tikkikierroksen pelaamiseen ja graafisen käyttöliittymän päivittämiseen.
"""
def play_trick(self, event, players_cards, continue_button, chicago_object):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_position = pygame.mouse.get_pos()
        trick_card_select(self, players_cards)
        if chicago_object[0] != 0:
            if chicago_object[0].collidepoint(mouse_position):
                if not chicago_object[1]:
                    color = (0, 200, 0)
                    draw_blanco_button(self, color)
                    chicago_object[1] = True
                    print(chicago_object)
                else:
                    color = (0, 0, 0)
                    draw_blanco_button(self, color)
                    chicago_object[1] = False
                    print(chicago_object)
            pygame.display.update()
            self.mode = 3
        if continue_button.collidepoint(mouse_position) and chicago_object[1]:
            self.chicago[self.players[self.turn]] = 1
            self.mode = 1
            self.start = self.players.index(self.players[self.turn])
            self.chicago_player = self.players[self.turn]
            self.chicago_successful = True
            self.chicago_on = True
            self.compare_card = None
            for card in self.played_cards:
                card[0].hand.append(card[1])
        if continue_button.collidepoint(mouse_position) and self.card_selected:
            print(self.chicago_successful)
            played_card = (0,0,0)
            for card in players_cards:
                if card[3]:
                    played_card = card[0]
                pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x-20,
                card[1].y-20, self.CARD_SIZE[0]+20, self.CARD_SIZE[1]+40))
            pygame.display.update()
            print(played_card)
            play_card(self, self.players[self.turn], played_card)
            print("ok")
            self.turn += 1
            if self.turn == len(self.players):
                self.turn = 0
            if self.turn == self.start:
                if len(self.players[self.start].hand) == 0:
                    print(self.compare_card[2])
                    print ("loppu")
                    self.dealing_turn += 1
                    if self.dealing_turn == len(self.players):
                        self.dealing_turn = 0
                    self.deals = 0
                    self.game_to_play = 1
                    self.deck = Deck()
                    self.start = self.dealing_turn
                    self.turn = self.dealing_turn
                    self.played_cards = []
                    self.round_ending_lines = []
                    random.shuffle(self.deck.cards)
                    self.deck.deal_cards(self.players)
                    end_trick(self)
                    if round_ending(self):
                        self.mode = 2
                        self.turn = 0
                        self.card_selected = False
                        self.played_cards = []
                        self.compare_card = None
                        self.start = 0
                        self.value_comparison = (0,0)
                        self.dealing_turn = 0
                        self.starting_player = 0
                        self.game_to_play = 0
                    else:
                        print_round_ending_lines(self)
                        time.sleep(5)
                    set_up_chicago(self)
                else:
                    if self.compare_card[2] != self.chicago_player:
                        self.chicago_successful = False
                    self.start = self.players.index(self.compare_card[2])
                    self.compare_card = None
                    self.turn = self.start
            if self.game_to_play == 2:
                print(self.players[self.turn].name)
            if self.mode == 3:
                self.mode = 1
            self.card_selected = False
    draw_continue_button(self)
    if chicago_object[0] != 0:
        if chicago_object[1]:
            color = (0, 200, 0)
            draw_chicago_button(self, color)
        else:
            color = (0, 0, 0)
            draw_chicago_button(self, color)
    pygame.display.update()

"""
Metodi tikkikierroksen päättämiseen.
"""
def end_trick(self):
    if self.chicago_on:
        if self.chicago_successful:
            if self.blanco_is_on:
                self.scoreboard[self.compare_card[2]] += 30
                self.round_ending_lines.append(self.compare_card[2].name
                                               + " sai läpi onnistuneesti blanco-chicagon.")
            else:
                self.scoreboard[self.compare_card[2]] += 15
                self.round_ending_lines.append(self.compare_card[2].name
                                               + " sai läpi onnistuneesti chicagon.")
        else:
            self.scoreboard[self.compare_card[2]] += 5
            self.round_ending_lines.append(self.compare_card[2].name 
                                           + " sai lopetuksen ja " + self.chicago_player.name
                                           + "n chicago meni pieleen.")
            if self.blanco_is_on:
                self.scoreboard[self.chicago_player] -= 30
            else:
                self.scoreboard[self.chicago_player] -= 15
    else:
        if self.compare_card[0] == 2:
            self.scoreboard[self.compare_card[2]] += 10
            self.round_ending_lines.append("Kierroksen lopetti " +
                  self.compare_card[2].name + " kakkoslopetuksella")
        else:
            self.scoreboard[self.compare_card[2]] += 5
            self.round_ending_lines.append("Kierroksen lopetti " 
                                           + self.compare_card[2].name)
"""
Metodi vertailukortin vaihtamiseen tikkiä varten.
"""
def set_compare_card(self, player, card):
    compare_card_number = card[0]
    compare_card_suit = card[1]
    compare_card_player = player
    self.compare_card = (compare_card_number, compare_card_suit, compare_card_player)
"""
Metodi kortin pelaamiseen tikissä.
"""
def play_card(self, player, played_card):
    i = 0
    playable_cards = []
    for card in player.hand:
        if self.compare_card is not None:
            if card[1] == self.compare_card[1]:
                playable_cards.append(card)
        else:
            playable_cards.append(card)
    if len(playable_cards) == 0:
        playable_cards = player.hand
    player.hand.remove(played_card)
    self.played_cards.append((player, played_card))
    print(played_card)
    if self.compare_card is None:
        set_compare_card(self, player, played_card)
    if played_card[1] == self.compare_card[1]:
        if played_card[0] > self.compare_card[0]:
            set_compare_card(self,player, played_card)
"""
Metodi pokerikäsien vertailuun.
"""
def compare_hands(hands):
    strongest_hand_object = (0, 0)
    strongest_hand = 0
    strongest_player = 0
    comparable_hands = [1, 3, 4, 5, 8, 10]
    same_hand = False
    same_value_but_different_numbers = False
    for hand in hands:
        if hand[1][0] > strongest_hand:
            same_hand = False
            same_value_but_different_numbers = False
            strongest_hand = hand[1][0]
            strongest_hand_object = hand[1]
            strongest_player = hand[0]
        elif hand[1][0] == strongest_hand:
            if hand[1][0] in comparable_hands:
                same_value_but_different_numbers = True
                if hand[1][1] > strongest_hand_object[1]:
                    strongest_hand = hand[1][0]
                    strongest_hand_object = hand[1]
                    strongest_player = hand[0]
                elif hand[1][1] == strongest_hand_object[1]:
                    same_hand = True
            if hand[1][0] == 2:
                same_hand = True
    if same_hand:
        return (0, strongest_hand, 2)
    if strongest_hand in comparable_hands and same_value_but_different_numbers:
        return (strongest_player, strongest_hand, 1)
    return (strongest_player, strongest_hand, 0)
"""
Metodi kierroksen päättämiseen ja pisteiden tarkistukseen.
"""
def round_ending(self):
    no_chicagos = True
    self.round_ending_lines.append("Uusi kierros alkaa...")
    for player in self.chicago:
        if self.chicago[player] != 0:
            no_chicagos = False
    if no_chicagos:
        end_game_poker_points(self)
    else:
        self.round_ending_lines.append("Kierroksella huudettiin chicago, ei pokeripisteitä.")
    points = []
    for player in self.players:
        points.append(self.scoreboard[player])
    points.sort()
    if points_check(self, points):
        return True
    print("")
    print("Uusi kierros.")
    print("")
    return False
"""
Metodi pistetarkistukseen ja pelin päättämiseen jos pisteitä on tarpeeksi.
"""
def points_check(self, points):
    if points[len(points)-1] >= 20:
        if points[len(points)-1] > points[len(points)-2]:
            for player in self.players:
                if self.scoreboard[player] == points[len(points)-1]:
                    self.winningtext.append("Peli päättynyt!")
                    self.winningtext.append("Voittaja on: " + player.name + ". Pisteet: "
                          + str(points[len(points)-1]))
        if points[len(points)-1] == points[len(points)-2]:
            self.winningtext.append("Pisteraja ylitetty, mutta osalla pelaajista on tasatilanne.")
            self.winningtext.append("Pelaajat tasatilanteessa: ", end=" ")
            for player in self.players:
                if self.scoreboard[player] == points[len(points)-1]:
                    self.winningtext.append(player.name + " ", end=" ")
            self.winningtext.append("Pisteillä: " + str(points[len(points)-1]))
        return True
    return False
"""
Metodi alku- ja loppuvalikon toimintoja varten.
"""
def menu_actions(self, event, button):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_position = pygame.mouse.get_pos()
        if button.collidepoint(mouse_position):
            if self.mode == 2:
                print("")
                print("Uusi peli aloitettu")
                print("")
                self.winningtext = []
                set_up_players(self)
                set_up_scoreboard(self)
                set_up_chicago(self)
            self.mode = 1
            self.game_to_play = 1
            random.shuffle(self.deck.cards)
            self.deck.deal_cards(self.players)
            print(poker_points(self))
