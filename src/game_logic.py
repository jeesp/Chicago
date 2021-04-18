import random
from player import Player
from deck import Deck
from game_actions import end_game_poker_comparison, play_poker, play_trick, compare_hands
def play():
    players = []
    player1 = Player('Ake')
    players.append(player1)
    player2 = Player('Make')
    players.append(player2)
    player3 = Player('Jake')
    players.append(player3)
    player4 = Player('Åke')
    players.append(player4)
    score_board = dict()
    for player in players:
        score_board[player] = 0
    hand_values = {0:"Ei mitään", 1:"Pari", 2:"Kaksi paria", 3:"Kolmoset", 4:"Suora",
     5:"Väri", 6:"Täyskäsi", 8:"Neloset", 10:"Värisuora"}
    points = 0
    deals = 0
    dealing_turn = 0
    while True:
        deck = Deck()
        while deals < 2:
            random.shuffle(deck.cards)
            deck.deal_cards(players)
            random.shuffle(deck.cards)
            deck.deal_cards(players)
            hands = []
            chicago = dict()
            for player in players:
                chicago[player] = 0
            play_poker(deck, chicago, deals, players, hands, score_board, hand_values, dealing_turn)
            deals += 1
        deck.deal_cards(players)
        value_comparison = compare_hands(hands)
        play_trick(dealing_turn,players,score_board, chicago)
        deals = 0
        dealing_turn += 1
        if dealing_turn == len(players):
            dealing_turn = 0
        no_chicagos = True
        for player in chicago:
            if chicago[player] != 0:
                no_chicagos = False
        if no_chicagos:
            end_game_poker_comparison(value_comparison, score_board, hand_values)
        else:
            print("Kierroksella huudettiin chicago, ei pokeripisteitä.")
        for player in score_board:
            print(player.name + ": ", score_board[player])
        points = []
        for player in players:
            points.append(score_board[player])
        points.sort()
        if points[len(points)-1] >= 10:
            if points[len(points)-1] > points[len(points)-2]:
                for player in players:
                    if score_board[player] == points[len(points)-1]:
                        print("Peli päättynyt!")
                        print("Voittaja on: " + player.name + ". Pisteet: "
                         + str(points[len(points)-1]))
            if points[len(points)-1] == points[len(points)-2]:
                print("Pisteraja ylitetty, mutta osalla pelaajista on tasatilanne.")
                print("Pelaajat tasatilanteessa: ", end=" ")
                for player in players:
                    if score_board[player] == points[len(points)-1]:
                        print(player.name + " ", end=" ")
                print("Pisteillä: " + str(points[len(points)-1]))
            break
def set_player(players, number):
    print(str(number)+ ". pelaajan nimi: ", end=" ")
    name = input()
    player = Player(name)
    players.append(player)
