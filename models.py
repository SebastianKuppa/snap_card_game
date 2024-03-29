import pygame
import random
from enum import Enum


class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/' + str(self.suit.name) + '-' + str(self.value) + '.svg')


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)


class Pile:
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def peek(self):
        if len(self.cards) > 0:
            return self.cards[-1]
        else:
            return None

    def popAll(self):
        return self.cards

    def clear(self):
        self.cards = []

    def isSnap(self):
        if len(self.cards) > 1:
            return self.cards[-1].value == self.cards[-2].value
        return False


class Player:
    def __init__(self, flipKey, snapKey, name):
        self.hand = []
        self.flipKey = flipKey
        self.snapKey = snapKey
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)



