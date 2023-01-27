from enum import Enum
import pygame
from models import *


class GameState(Enum):
    PLAYING = 0
    SNAPPING = 1
    ENDED = 2


class GameEngine:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player(name='Player1', flipKey=pygame.K_q, snapKey=pygame.K_w)
        self.player2 = Player(name='Player2', flipKey=pygame.K_o, snapKey=pygame.K_p)
        self.pile = Pile()
        self.deal()
        self.current_player = self.player1
        self.state = GameState.PLAYING

    def deal(self):
        half = self.deck.cards.length() // 2
        for i in range(0, half):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    def switchPlayer(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
