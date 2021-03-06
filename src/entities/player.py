class Player:
    """
    Luokka pelaajalle. Pelaajalla on nimi ja käsi.
    """
    def __init__(self, name):
        self.name = name
        self.hand = []
    def remove_card(self, card):
        """
        Metodi poistaa kortin pelaajan kädestä.
        """
        self.hand.remove(card)
    def hand_value(self):
        """
        Metodi laskee pelaajan käden arvon.
        """
        player = self
        suits = set()
        numbers = []
        for card in player.hand:
            numbers.append(card[0])
            suits.add(card[1])
        numbers.sort()
        if self.check_straight_and_flush(suits, numbers) is not None:
            return self.check_straight_and_flush(suits, numbers)
        if self.check_same_numbers(numbers) is not None:
            return self.check_same_numbers(numbers)
        return (0, 0)
    def check_same_numbers(self, numbers):
        """
        Metodi tarkistaa onko kädessä arvoltaan samoja kortteja.
        """
        same_numbers = dict()
        for i in range(0, 5):
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
        if Player.check_pairs_and_three_of_a_kind(self, same_numbers,
                                                  three_of_a_kind, two_pairs, pair) is not None:
            return Player.check_pairs_and_three_of_a_kind(self, same_numbers,
                                                          three_of_a_kind, two_pairs, pair)
        return None
    def check_pairs_and_three_of_a_kind(self, same_numbers, three_of_a_kind, two_pairs, pair):
        """
        Metodi tarkistaa parit ja kolmoset.
        """
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
        """
        Metodi tarkistaa värin ja suoran.
        """
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
                    if numbers[i] - numbers[i-1] != 1:
                        if numbers[i] != 14 and numbers[i-1] != 1:
                            straight = False
                            del numbers[0]
                            break
                    i += 1
        else:
            for i in range(1, 5):
                if numbers[i] - numbers[i-1] != 1:
                    straight = False
                    break
        if flush and straight:
            return (52, numbers[len(numbers)-1])
        if flush:
            return (5, numbers[len(numbers)-1])
        if straight:
            return (4, numbers[len(numbers)-1])
        return None
