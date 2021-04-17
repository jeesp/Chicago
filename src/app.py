import random
from player import Player
from deck import Deck

def main():
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
    print(score_board)
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
            play_poker(deck, players, hands, score_board, hand_values, dealing_turn)
            deals += 1
        deck.deal_cards(players)
        value_comparison = compare_hands(hands)
        play_trick(dealing_turn,players,score_board)
        deals = 0
        dealing_turn += 1
        if dealing_turn == len(players):
            dealing_turn = 0
        end_game_poker_comparison(value_comparison, score_board, hand_values)
        print(score_board)
        points = []
        for player in players:
            points.append(score_board[player])
        points.sort()
        if points[len(points)-1] >= 20:
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
def end_game_poker_comparison(value_comparison, score_board, hand_values):
    if value_comparison[0] != 0:
        score_board[value_comparison[0]] += value_comparison[1]
        if value_comparison[2] == 0:
            print("Lopun pokeripisteet sai: " + value_comparison[0].name + ". Käsi: "
             + hand_values[value_comparison[1]].lower() + ".")
        if value_comparison[2] == 1:
            print("Lopun pokeripisteet sai: " + value_comparison[0].name + ". Käsi: "
             + hand_values[value_comparison[1]].lower() + ". Myös toisella pelaajalla oli "
             + hand_values[value_comparison[1]].lower() + ".")
    else:
        if value_comparison[2] == 2:
            print("Kahdella pelaajalla oli sama käsi: "
             + hand_values[value_comparison[1]].lower()
             + ". Kukaan ei saanut pisteitä.")
        else:
            print("Kenelläkään ei ollut mitään, joten kukaan ei saanut lopun pokeripisteitä.")
def play_poker(deck, players, hands, score_board, hand_values, dealing_turn):
    for player in players:
        hand = player.hand_value()
        hands.append((player, hand))
    value_comparison = compare_hands(hands)
    if value_comparison[0] != 0:
        score_board[value_comparison[0]] += value_comparison[1]
        if value_comparison[2] == 0:
            print("Pisteet sai: " + value_comparison[0].name + ". Käsi: "
             + hand_values[value_comparison[1]].lower() + ".")
        if value_comparison[2] == 1:
            print("Pisteet sai: " + value_comparison[0].name + ". Käsi: "
             + hand_values[value_comparison[1]].lower() + ". Myös toisella pelaajalla oli "
             + hand_values[value_comparison[1]].lower() + ".")
    else:
        if value_comparison[2] == 2:
            print("Kahdella pelaajalla on sama käsi: "
             + hand_values[value_comparison[1]].lower()
             + ". Kukaan ei saanut pisteitä.")
        else:
            print("Kenelläkään ei ollut mitään, joten kukaan ei saanut pisteitä.")
    print(score_board)
    for hand in hands:
        print (hand[0].name+"n käsi: ", hand_values[hand[1][0]].lower())
    print("Valitse vaihdettavat kortit: ")
    turn = dealing_turn
    change_card(hands[turn], deck)
    turn += 1
    if turn == len(players):
        turn = 0
    while turn != dealing_turn:
        change_card(hands[turn], deck)
        turn += 1
        if turn == len(players):
            turn = 0
def play_trick(dealing_turn, players, score_board):
    start = dealing_turn
    compare_card = (0,0,0)
    while len(players[0].hand) > 0:
        compare_card = None
        compare_card = play_card(players[start], compare_card)
        print(compare_card)
        turn = start + 1
        if turn == len(players):
            turn = 0
        while turn != start:
            compare_card = play_card(players[turn], compare_card)
            turn += 1
            if turn == len(players):
                turn = 0
        start = players.index(compare_card[2])
    if compare_card[0] == 2:
        score_board[compare_card[2]] += 10
        print("Kierroksen lopetti " + compare_card[2].name + " kakkoslopetuksella")
    else:
        score_board[compare_card[2]] += 5
        print("Kierroksen lopetti " + compare_card[2].name)
def set_compare_card(player,card):
    compare_card_number = card[0]
    compare_card_suit = card[1]
    compare_card_player = player
    return (compare_card_number, compare_card_suit, compare_card_player)
def change_card(hand, deck):
    print(hand[0].name + ", mitä vaihdetaan? Anna indeksi")
    i = 0
    while i < len(hand[0].hand):
        print(str(i) + ": " + hand[0].hand[i][2])
        i += 1
    changecards_ids = input("Syötä indeksit pilkulla erotettuna: ")
    print (changecards_ids)
    changedcards_ids_as_list = changecards_ids.split(",")
    print(changedcards_ids_as_list)
    cards_to_change = []
    if changecards_ids != "":
        for changecard_id in changedcards_ids_as_list:
            cards_to_change.append(hand[0].hand[int(changecard_id)])
        for card in cards_to_change:
            deck.add_card_to_dealt_cards(card)
            hand[0].remove_card(card)
    print (cards_to_change)
def play_card(player, compare_card):
    i = 0
    playable_cards = []
    for card in player.hand:
        if compare_card is not None:
            if card[1] == compare_card[1]:
                playable_cards.append(card)
        else:
            playable_cards.append(card)
    if len(playable_cards) == 0:
        playable_cards=player.hand
    while i < len(player.hand):
        if player.hand[i] in playable_cards:
            print(str(i) + ": " + player.hand[i][2])
        else:
            print("X: " + player.hand[i][2])
        i += 1
    played_card_index = int(input(player.name + ", mikä kortti pelataan? Anna indeksi: "))
    played_card = player.hand[played_card_index]
    player.hand.remove(played_card)
    print(played_card)
    if compare_card is None:
        return set_compare_card(player,played_card)
    if played_card[1] == compare_card[1]:
        if played_card[0] > compare_card[0]:
            return set_compare_card(player,played_card)
    return compare_card

def set_player(players, number):
    print(str(number)+ ". pelaajan nimi: ", end=" ")
    name = input()
    player = Player(name)
    players.append(player)
def compare_hands(hands):
    strongest_hand_object = (0,0)
    strongest_hand = 0
    strongest_player = 0
    comparable_hands = [1,3,4,5,8,10]
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


if __name__ == "__main__":
    main()
