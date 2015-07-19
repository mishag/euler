#!/usr/bin/python

"""
poker hands
"""

import sys

TWO   = 2
THREE = 3
FOUR  = 4
FIVE  = 5
SIX   = 6
SEVEN = 7
EIGHT = 8
NINE  = 9
TEN   = 10
JACK  = 11
QUEEN = 12
KING  = 13
ACE   = 14

HEARTS   = 200
DIAMONDS = 300
CLUBS    = 400
SPADES   = 500

STRING_TO_VALUE = {
    "2" : TWO,
    "3" : THREE,
    "4" : FOUR,
    "5" : FIVE,
    "6" : SIX,
    "7" : SEVEN,
    "8" : EIGHT,
    "9" : NINE,
    "T": TEN,
    "J" : JACK,
    "Q" : QUEEN,
    "K" : KING,
    "A" : ACE
}

STRING_TO_SUIT = {
    "H" : HEARTS,
    "D" : DIAMONDS,
    "C" : CLUBS,
    "S" : SPADES
}

VALUES = set(STRING_TO_VALUE.values())
SUITS  = set(STRING_TO_SUIT.values())

VALUE_TO_STRING = {
    TWO   : "2",
    THREE : "3",
    FOUR  : "4",
    FIVE  : "5",
    SIX   : "6",
    SEVEN : "7",
    EIGHT : "8",
    NINE  : "9",
    TEN   : "T",
    JACK  : "J",
    QUEEN : "Q",
    KING  : "K",
    ACE   : "A"
}

SUIT_TO_STRING = {
    HEARTS   : "H",
    DIAMONDS : "D",
    CLUBS    : "C",
    SPADES   : "S"
}

NO_HAND         = 0
ONE_PAIR        = 1
TWO_PAIRS       = 2
THREE_OF_A_KIND = 3
STRAIGHT        = 5
FLUSH           = 10
FULL_HOUSE      = 40
FOUR_OF_A_KIND  = 100
STRAIGHT_FLUSH  = 200
ROYAL_FLUSH     = 500


class Card:
    
    def __init__(self, value, suit):
        if value not in VALUES or suit not in SUITS:
            error = "Invalid value or suit (%s %s)" %(value, suit)
            raise RuntimeError(error)
        
        self._value = value
        self._suit  = suit

    def __str__(self):
        if self._value in VALUES and self._suit in SUITS:
            return ''.join([VALUE_TO_STRING[self._value],
                            SUIT_TO_STRING[self._suit]])

        return ""

    def __repr__(self):
        if self._value in VALUES and self._suit in SUITS:
            return ''.join([VALUE_TO_STRING[self._value],
                            SUIT_TO_STRING[self._suit]])

        return ""


    def from_string(self, s):
        if len(s) != 2:
            return None

        value = STRING_TO_VALUE.get(s[0])
        suit  = STRING_TO_SUIT.get(s[1])

        if value is None or suit is None:
            return None

        self._value = value
        self._suit  = suit

        return self
    
    def value(self):
        return self._value

    def suit(self):
        return self._suit


def get_value_map(cards):
    value_map = {}
    for card in cards:
        num_vals = value_map.get(card.value(), 0)
        value_map[card.value()] = num_vals + 1

    return value_map


class Hand:
    def __init__(self, card_list):
        if len(card_list) != 5:
            raise RuntimeError("Expecting 5 cards in a hand.")

        card_list = sorted(card_list, key=lambda card: card.value())
        
        self._cards = card_list

    def __str__(self):
        return str(self._cards)

    def __repr__(self):
        return str(self._cards)

    # return highest ranked card if flush, 0 otherwise
    def has_flush(self):
        suits = set([x.suit() for x in self._cards])
        if len(suits) == 1:
            return self._cards[-1].value()

        return 0
    
    def has_straight(self):
        for i, card in enumerate(self._cards):
            if 0 == i:
                continue
            if self._cards[i].value() - self._cards[i-1].value() != 1:
                return 0

        return self._cards[-1].value()
        
    def has_straight_flush(self):
        if self.has_flush() and self.has_straight():
            return self._cards[-1].value()

        return 0

    def is_royal_flush(self):
        return self._cards[0].value() == TEN and self.has_straight_flush()

    # return the value of the 4 cards or 0 otherwise
    def is_four_of_a_kind(self):
        cards = self._cards
        if (cards[0].value() == cards[1].value() and
            cards[1].value() == cards[2].value() and
            cards[2].value() == cards[3].value()):
            return cards[0].value()

        if (cards[1].value() == cards[2].value() and
            cards[2].value() == cards[3].value() and
            cards[3].value() == cards[4].value()):
            return cards[1].value()

        return 0
        
    def is_full_house(self):
        cards = self._cards
        if ( (cards[0].value() == cards[1].value()) and
             (cards[2].value() == cards[3].value() and
              cards[3].value() == cards[4].value()) ):
            return cards[2].value()

        if ( (cards[0].value() == cards[1].value() and
              cards[1].value() == cards[2].value()) and
             (cards[3].value() == cards[4].value()) ):
            return cards[0].value()

        return 0

    def has_three_of_a_kind(self):
        cards = self._cards
        
        if (cards[0].value() == cards[1].value() and
            cards[1].value() == cards[2].value()):
            return cards[0].value()

        if (cards[1].value() == cards[2].value() and
            cards[2].value() == cards[3].value()):
            return cards[1].value()
        
        if (cards[2].value() == cards[3].value() and
            cards[3].value() == cards[4].value()):
            return cards[2].value()

        return 0
        
    def is_a_pair(self):
        value_map = get_value_map(self._cards)
        pair_values = []
        for card_value, num_cards in value_map.iteritems():
            if num_cards == 2:
                pair_values.append(card_value)

        if len(pair_values) == 1:
            return max(pair_values)

        return 0
        

    def is_two_pair(self):
        value_map = get_value_map(self._cards)
        pair_values = []
        for card_value, num_cards in value_map.iteritems():
            if num_cards == 2:
                pair_values.append(card_value)

        if len(pair_values) == 2:
            return max(pair_values)

        return 0

    # return rank of the hand and the highest card in the rank
    def get_hand_value(self):
        if self.is_royal_flush():
            return ROYAL_FLUSH, ACE
        
        if self.has_straight_flush():
            return STRAIGHT_FLUSH, self._cards[-1].value()
        
        val = self.is_four_of_a_kind()
        if val: 
            return FOUR_OF_A_KIND, val

        val = self.is_full_house()
        if val:
            return FULL_HOUSE, val

        val = self.has_flush()
        if val:
            return FLUSH, val

        val = self.has_straight()
        if val:
            return STRAIGHT, val

        val = self.has_three_of_a_kind()
        if val:
            return THREE_OF_A_KIND, val

        val = self.is_two_pair()
        if val:
            return TWO_PAIRS, val

        val = self.is_a_pair()
        if val:
            return ONE_PAIR, val

        return NO_HAND, self._cards[-1].value()

    def __gt__(self, other):
        selfHand, selfHigh = self.get_hand_value()
        otherHand, otherHigh = other.get_hand_value()

        print "(%d, %d) vs (%d, %d)" %(selfHand, selfHigh, otherHand, otherHigh),

        if selfHand > otherHand:
            print " One"
            return True
        elif otherHand > selfHand:
            print " Two"
            return False

        if selfHigh > otherHigh:
            print " One"
            return True
        elif otherHigh > selfHigh:
            print " Two"
            return False

        if ( max([card.value() for card in self._cards]) >
             max([card.value() for card in other._cards]) ):
            print " One"
            return True        

        print " Two"
        return False
            

def card_from_string(str):
    return Card(STRING_TO_VALUE[str[0]],
                STRING_TO_SUIT[str[1]])

def hand_from_string(str):
    str_list = str.split(' ')
    card_list = [card_from_string(str) for str in str_list]
    return Hand(card_list)

def generate_hands(file_name):
    
    try:
        input_file = open(file_name, 'r')
        list_of_hands = []
        for line in input_file:
            cards = [card_from_string(c) for c in line.strip().split(' ')]
            list_of_hands.append((Hand(cards[0:5]), Hand(cards[5:10])))

        return list_of_hands
    
    except IOError:
        print "Failed to open file %s" %file_name
        return None
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Expecting an input file."
        exit(-1)

    num_wins = 0

    list_of_hands = generate_hands(sys.argv[1])    
    for hand_pair in list_of_hands:
        hand_one = hand_pair[0]
        hand_two = hand_pair[1]
        print " %s, %s " %(hand_one, hand_two),
        if hand_one > hand_two:
            num_wins += 1

    print num_wins
