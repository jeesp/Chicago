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
    tulostaulukko = []
    hand_values = {0:"Ei mitään", 1:"Pari", 2:"Kaksi paria", 3:"Kolmoset", 4:"Suora", 5:"Väri", 6:"Täyskäsi", 8:"Neloset", 10:"Värisuora"}
    
    while True:
        deck = Deck()
        random.shuffle(deck.cards)
        deck.deal_cards(players)
        hands = []
        for player in players:
            hand = player.hand_value()
            hands.append((player, hand))
        comparing = compare_hands(hands)
        
        if comparing[0] != 0:
            if comparing[2] == 0:
                print("Pisteet sai: " +comparing[0].name + ". Käsi: " + hand_values[comparing[1]].lower() + ".")
            if comparing[2] == 1:
                print("Pisteet sai: " +comparing[0].name + ". Käsi: " + hand_values[comparing[1]].lower() + ". Myös toisella pelaajalla oli " + hand_values[comparing[1]].lower() + ".")
            if comparing[2] == 2:
                print("Kahdella pelaajalla on sama käsi: " + hand_values[comparing[1]].lower() + ".")
        else:
            print("Kierrokselta kukaan ei saanut pisteitä.")
        for hand in hands:
            print (hand[0].name+"n käsi: ", hand_values[hand[1][0]].lower())
        break
def set_player(players, number):
    print(str(number)+ ". pelaajan nimi: ", end=" ")
    name = input()
    player = Player(name)
    players.append(player)
def compare_hands(hands):
    strongest_hand_object = 0
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
        return (-1, strongest_hand, 2)
    if strongest_hand in comparable_hands and same_value_but_different_numbers:
        return (strongest_player, strongest_hand, 1)
    return (strongest_player, strongest_hand, 0)


if __name__ == "__main__": main()