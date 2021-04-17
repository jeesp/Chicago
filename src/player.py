class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def remove_card(self, card):
        self.hand.remove(card)
    def hand_value(self):
        player = self
        suits = set()
        numbers = []
        for card in player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        if Player.check_straight_and_flush(self, suits, numbers) is not None:
            return Player.check_straight_and_flush(self, suits, numbers)
        if Player.check_same_numbers(self,numbers) is not None:
            return Player.check_same_numbers(self,numbers)
        return (0,0)
    def check_same_numbers(self,numbers):
        same_numbers = dict()
        for i in range(0,5):
            if numbers[i] not in same_numbers:
                same_numbers[numbers[i]] = 1
            else:
                same_numbers[numbers[i]] += 1
        three_of_a_kind = False
        two_pairs = False
        pair = False
        for number in same_numbers:
            if same_numbers[number] == 4:
                return (8, number)
            if (same_numbers[number] == 2 and three_of_a_kind) \
                or (same_numbers[number] == 3 and pair):
                return (6, 1)
            if same_numbers[number] == 3:
                three_of_a_kind = True
            if same_numbers[number] == 2 and pair:
                two_pairs = True
            if same_numbers[number] == 2:
                pair = True
        if Player.check_pairs_and_three_of_a_kind(self, same_numbers, \
            three_of_a_kind, two_pairs, pair) is not None:
            return Player.check_pairs_and_three_of_a_kind(self, same_numbers, \
                three_of_a_kind, two_pairs, pair)
        return None
    def check_pairs_and_three_of_a_kind(self, same_numbers, three_of_a_kind, two_pairs, pair):
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
        return None
    def check_straight_and_flush(self, suits, numbers):
        flush = False
        straight = True
        if len(suits) == 1:
            flush = True
        if numbers[len(numbers)-1] == 14:
            if numbers[len(numbers)-2] == 14:
                straight = False
            else:
                numbers.append(1)
                numbers.sort()
                i = 1
                while i < len(numbers):
                    if numbers[i]- numbers[i-1] != 1:
                        straight = False
                        numbers.remove(1)
                        break
                    i += 1
        else:
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
        return None
