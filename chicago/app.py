import random
def main():
    players = []
    player1 = ('Ake', [])
    players.append(player1)
    player2 = ('Make', [])
    players.append(player2)
    player3 = ('Jake', [])
    players.append(player3)
    player4 = ('Åke', [])
    players.append(player4)
    tulostaulukko = []
    hand_values = {"Pair":1, "Two pairs":2, "Three of a kind": 3, "Straight": 4, "Flush": 5, "Full house": 6, "Four of a kind": 8, "Straight flush": 10}
    
    while True:
        print (players)
        cards = get_cards()
        random.shuffle(cards)
        dealt_cards = []
        for player in players:
            while len(player[1]) < 5:
                deal_card(player, cards, dealt_cards)
            print (player)
        print (compare_hands(players)[1])
        break
def set_player(players, number):
    print(str(number)+ ". pelaajan nimi: ", end=" ")
    player = input()
    hand = []
    players.append((player, hand))

def get_cards():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    cards = []
    for suit in suits:
        for number in numbers:
            if number == 1:
                number_string = 'ace'
            else:
                number_string = str(number)
            cards.append((number, suit, number_string+"_of_"+suit))
    return cards

def deal_card(player, cards, dealt_cards):
    if len(cards) > 0:
        card = cards[0]
        cards.remove(card)
        dealt_cards.append(card)
        player[1].append(card)

def compare_hands(players):
    strongest_hand_object = 0
    strongest_hand = 0
    strongest_player = 0
    same_hand = False
    for player in players:
        hand_object = hand_value(player)
        if hand_object[0] > strongest_hand:
            strongest_hand = hand_object[0]
            strongest_hand_object = hand_object
            strongest_player = player
        elif hand_object[0] == strongest_hand:
            if hand_object[0] == 1:
                if hand_object[1] > strongest_hand_object[1]:
                    strongest_hand = hand_object[0]
                    strongest_hand_object = hand_object
                    strongest_player = player
                if hand_object[1] == strongest_hand_object[1]:
                    same_hand = True
    return (strongest_player, strongest_hand)

def hand_value(player):
    suits = set()
    numbers = []
    for card in player[1]:
        numbers.append(card[0])
        suits.add(card[1])
    numbers.sort()
    flush = False
    straight = True

    if len(suits) == 1:
        flush = True
    for i in range(1,5):
        if numbers[i] - numbers[i-1] != 1:
            straight = False
            break
    if flush and straight:
        return (10, numbers[len(numbers)-1])
    if flush:
        return (5, numbers[len(numbers)-1])
    if straight:
        return (4, numbers[len(numbers)-1])
    
    same_numbers = dict()

    for i in range(1,5):
        if numbers[i] not in same_numbers:
            same_numbers[numbers[i]] = 1
        else:
            same_numbers[numbers[i]] += 1
    four_of_a_kind = False
    full_house = False
    three_of_a_kind = False
    two_pairs = False
    pair = False
    for number in same_numbers:
        if same_numbers[number] == 4:
            four_of_a_kind = True
            return (8, number)
        if same_numbers[number] == 2 and three_of_a_kind:
            full_house = True
            return (6, number)
        if same_numbers[number] == 3:
            three_of_a_kind = True
        if same_numbers[number] == 2 and pair:
            two_pairs = True
        if same_numbers[number] == 2:
            pair = True
    if three_of_a_kind:
        for number in same_numbers:
            if same_numbers[number] == 3:
                return (3, number)
    if two_pairs:
        return (2, 0)
    if pair:
        for number in same_numbers:
            if same_numbers[number] == 2:
                return (1, number)
    return (-1, 0)
if __name__ == "__main__": main()