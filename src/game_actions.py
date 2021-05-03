import time
import random
import pygame
from entities.deck import Deck
from entities.player import Player
def end_game_poker_comparison(self):
    if self.value_comparison[0] != 0:
        self.scoreboard[self.value_comparison[0]] += self.value_comparison[1]
        if self.value_comparison[2] == 0:
            return ("Lopun pokeripisteet sai: " + self.value_comparison[0].name + ". Käsi: "
                  + self.hand_values[self.value_comparison[1]].lower() + ".")
        if self.value_comparison[2] == 1:
            return ("Lopun pokeripisteet sai: " + self.value_comparison[0].name + ". Käsi: "
                  + self.hand_values[self.value_comparison[1]].lower() +
                  ". Myös toisella pelaajalla oli "
                  + self.hand_values[self.value_comparison[1]].lower() + ".")
    if self.value_comparison[2] == 2:
        return ("Kahdella pelaajalla oli sama käsi: "
              + self.hand_values[self.value_comparison[1]].lower()
              + ". Kukaan ei saanut pisteitä.")
    return ("Kenelläkään ei ollut mitään, joten kukaan ei saanut lopun "
            + "pokeripisteitä.")
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
def set_up_scoreboard(self):
    self.scoreboard = dict()
    for player in self.players:
        self.scoreboard[player] = 0
def poker_points(self):
    hands = []
    lines_to_print = []
    for player in self.players:
        hand = player.hand_value()
        hands.append((player, hand))
    self.value_comparison = compare_hands(hands)
    if self.value_comparison[0] != 0:
        self.scoreboard[self.value_comparison[0]] += self.value_comparison[1]
        
        if self.value_comparison[2] == 0:
            rivi = str("Pisteet sai: " + self.value_comparison[0].name + ". Käsi: " 
            + self.hand_values[self.value_comparison[1]].lower() + ".")
            lines_to_print.append(rivi)
        if self.value_comparison[2] == 1:
            rivi = str("Pisteet sai: " + self.value_comparison[0].name + ". Käsi: "
            + self.hand_values[self.value_comparison[1]].lower()
            + ". Myös toisella pelaajalla oli "
            + self.hand_values[self.value_comparison[1]].lower() + ".")
            lines_to_print.append(rivi)
    elif self.value_comparison[2] == 2:
        rivi = str("Kahdella pelaajalla on sama käsi: "
        + self.hand_values[self.value_comparison[1]].lower()
        + ". Kukaan ei saanut pisteitä.")
        lines_to_print.append(rivi)
    else:
        lines_to_print.append("Kenelläkään ei ollut mitään, joten kukaan ei saanut pisteitä.")
    for player in self.scoreboard:
        rivi = str(player.name) + ": " + str(self.scoreboard[player])
        lines_to_print.append(rivi)
    for hand in hands:
        rivi = str(hand[0].name)+"n käsi: " + str(self.hand_values[hand[1][0]].lower())
        lines_to_print.append(rivi)
    return lines_to_print
def play_poker(self, event, players_cards, continue_button):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_position = pygame.mouse.get_pos()
        for card in players_cards:
            if card[1].collidepoint(mouse_position):
                pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x,
                card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                pygame.display.flip()
                x_change = 5
                y_change = 15
                if card[3] == False:
                    pygame.draw.rect(self.screen, (25,25,25), pygame.Rect(card[1].x,
                    card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                    card[1].x += x_change
                    card[1].y -= y_change
                    card[3] = True
                else:
                    card[1].x -= x_change
                    card[1].y += y_change
                    card[3] = False
                self.screen.blit(card[2], card[1])
                pygame.display.update()
                self.mode = 3
                print(card)
                print(self.turn)
        if continue_button.collidepoint(mouse_position):
            cards_clicked = []
            for card in players_cards:
                if card[3]:
                    cards_clicked.append(card[0])
                pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x-20,
                card[1].y-20, self.CARD_SIZE[0]+20, self.CARD_SIZE[1]+40))
            pygame.display.update()
            print(cards_clicked)
            change_card(self, self.players[self.turn], cards_clicked)
            print("ok")
            self.turn += 1
            if self.turn == len(self.players):
                self.turn = 0
            if self.turn == self.dealing_turn:
                chicago = dict()
                for player in self.players:
                    chicago[player] = 0
                random.shuffle(self.deck.cards)
                self.deck.deal_cards(self.players)
                self.deals += 1
                if self.deals < 2:
                    print(poker_points(self))
                if self.deals == 2:
                    self.game_to_play = 2
                    self.turn = self.start
                    self.deals = 3
                    print(self.players[self.turn].name)
                    hands = []
                    for player in self.players:
                        hand = player.hand_value()
                        hands.append((player, hand))
                    self.value_comparison = compare_hands(hands)
            self.mode= 1
def change_card(self, player, cards_clicked):
    for card in cards_clicked:
        self.deck.add_card_to_dealt_cards(card)
        player.remove_card(card)
def play_trick(self, event, players_cards, continue_button):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_position = pygame.mouse.get_pos()
        for card in players_cards:
            if card[1].collidepoint(mouse_position):
                pygame.draw.rect(self.screen, self.POKER_GREEN, pygame.Rect(card[1].x,
                card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                pygame.display.flip()
                x_change = 5
                y_change = 15
                if card[3] == False and self.card_selected == False:
                    pygame.draw.rect(self.screen, (25,25,25), pygame.Rect(card[1].x,
                    card[1].y, self.CARD_SIZE[0], self.CARD_SIZE[1]))
                    card[1].x += x_change
                    card[1].y -= y_change
                    card[3] = True
                    self.card_selected = True
                elif card[3] == True and self.card_selected == True:
                    card[1].x -= x_change
                    card[1].y += y_change
                    card[3] = False
                    self.card_selected = False
                self.screen.blit(card[2], card[1])
                pygame.display.update()
                self.mode = 3
                print(card)
        if continue_button.collidepoint(mouse_position) and self.card_selected:
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
                    random.shuffle(self.deck.cards)
                    self.deck.deal_cards(self.players)
                    chicago_on = False
                    chicago_successful = False
                    chicago_player = None
                    blanco_is_on = False
                    end_trick(self, chicago_on, chicago_successful, chicago_player, blanco_is_on)
                    chicago = dict()
                    for player in self.players:
                        chicago[player] = 0
                    if round_ending(self, chicago):
                        self.mode = 2
                        self.turn = 0
                        self.card_selected = False
                        self.played_cards = []
                        self.compare_card = None
                        self.start = 0
                        self.value_comparison = (0,0)
                        self.dealing_turn = 0
                        self.starting_player = 0
                    else:
                        print(poker_points(self))
                else:
                    self.start = self.players.index(self.compare_card[2])
                    self.compare_card = None
                    self.turn = self.start
            if self.game_to_play == 2:
                print(self.players[self.turn].name)
            if self.mode == 3:
                self.mode = 1
            self.card_selected = False
#def play_trick(dealing_turn, players, scoreboard, chicago):
#    start = dealing_turn
#    compare_card = (0, 0, 0)
#    no_chicago = True
#    played_cards = []
#    for player in chicago:
#        if chicago[player] != 0:
#            start = players.index(player)
#            no_chicago = False
#    if no_chicago:
#        start = trick_no_chicago_first_round(
#            players, start, no_chicago, chicago, played_cards)
#    chicago_on = False
#    chicago_successful = True
#    chicago_player = None
#    blanco_is_on = False
#    for player in chicago:
#        if chicago[player] != 0:
#            chicago_on = True
#            chicago_player = player
#            if chicago[player] == 2:
#                blanco_is_on = True
#    while len(players[0].hand) > 0:
#        compare_card = None
#        compare_card = play_card(players[start], compare_card, played_cards)
#        print(compare_card)
#        turn = start + 1
#        if turn == len(players):
#            turn = 0
#        while turn != start:
#            compare_card = play_card(players[turn], compare_card, played_cards)
#            turn += 1
#            if turn == len(players):
#                turn = 0
#        start = players.index(compare_card[2])
#        if chicago_on:
#            if compare_card[2] != chicago_player:
#                chicago_successful = False
#    end_trick(chicago_on, chicago_successful, chicago_player, blanco_is_on,
#              compare_card, scoreboard)
#
#
def trick_no_chicago_first_round(players, start, no_chicago, chicago, played_cards):
    print(players[start].name + ", huudatko chicagon? y/n")
    answer = input()
    if answer == "y":
        print(players[start].name + " huusi chicagon")
        no_chicago = False
        chicago[players[start]] = 1
    compare_card = None
    compare_card = play_card(players[start], compare_card, played_cards)
    print(compare_card)
    turn = start + 1
    if turn == len(players):
        turn = 0
    while turn != start:
        if no_chicago:
            print(players[turn].name + ", huudatko chicagon? y/n")
            answer = input()
            if answer == "y":
                print(players[turn].name + " huusi chicagon")
                no_chicago = False
                chicago[players[turn]] = 1
                for card in played_cards:
                    card[0].hand.append(card[1])
                start = players.index(players[turn])
                return start
        compare_card = play_card(players[turn], compare_card, played_cards)
        turn += 1
        if turn == len(players):
            turn = 0
def end_trick(self, chicago_on, chicago_successful, chicago_player, blanco_is_on):
    if chicago_on:
        if chicago_successful:
            if blanco_is_on:
                self.scoreboard[self.compare_card[2]] += 30
                print(self.compare_card[2].name +
                      " sai läpi onnistuneesti blanco-chicagon.")
            else:
                self.scoreboard[self.compare_card[2]] += 15
                print(self.compare_card[2].name +
                      " sai läpi onnistuneesti chicagon.")
        else:
            self.scoreboard[self.compare_card[2]] += 5
            print(self.compare_card[2].name + " sai lopetuksen ja " + chicago_player.name
                  + "n chicago meni pieleen.")
            if blanco_is_on:
                self.scoreboard[chicago_player] -= 30
            else:
                self.scoreboard[chicago_player] -= 15
    else:
        if self.compare_card[0] == 2:
            self.scoreboard[self.compare_card[2]] += 10
            print("Kierroksen lopetti " +
                  self.compare_card[2].name + " kakkoslopetuksella")
        else:
            self.scoreboard[self.compare_card[2]] += 5
            print("Kierroksen lopetti " + self.compare_card[2].name)
def set_compare_card(self, player, card):
    compare_card_number = card[0]
    compare_card_suit = card[1]
    compare_card_player = player
    self.compare_card = (compare_card_number, compare_card_suit, compare_card_player)
#
#def change_card(hand, deck, chicago, deals):
#    no_blancos = True
#    for player in chicago:
#        if chicago[player] != 0:
#            no_blancos = False
#    if deals == 1 and no_blancos:
#        print("Huudatko blanco-chicagon?")
#        print(hand[0].name + "? y/n")
#        answer = input()
#        if answer == "y":
#            chicago[hand[0]] = 2
#            print(hand[0].name + " huusi blanco-chicagon")
#    print(hand[0].name + ", mitä vaihdetaan? Anna indeksi")
#    i = 0
#    while i < len(hand[0].hand):
#        print(str(i) + ": " + hand[0].hand[i][2])
#        i += 1
#    changecards_ids = input("Syötä indeksit pilkulla erotettuna: ")
#    print(changecards_ids)
#    changedcards_ids_as_list = changecards_ids.split(",")
#    print(changedcards_ids_as_list)
#    cards_to_change = []
#    if changecards_ids != "":
#        for changecard_id in changedcards_ids_as_list:
#            cards_to_change.append(hand[0].hand[int(changecard_id)])
#        for card in cards_to_change:
#            deck.add_card_to_dealt_cards(card)
#            hand[0].remove_card(card)
#    print(cards_to_change)
#
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
def round_ending(self, chicago):
    no_chicagos = True
    for player in chicago:
        if chicago[player] != 0:
            no_chicagos = False
    if no_chicagos:
        print (end_game_poker_comparison(self))
    else:
        print("Kierroksella huudettiin chicago, ei pokeripisteitä.")
    for player in self.scoreboard:
        print(player.name + ": ", self.scoreboard[player])
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
def points_check(self, points):
    if points[len(points)-1] >= 5:
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
            self.mode = 1
            self.game_to_play = 1
            random.shuffle(self.deck.cards)
            self.deck.deal_cards(self.players)
            print(poker_points(self))
