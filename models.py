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
        self.image = pygame.image.load('images/' + self.suit + '-' + str(self.value) + '.svg')


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



