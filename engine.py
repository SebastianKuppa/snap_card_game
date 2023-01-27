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
        self.deck.deal()
        self.current_player = self.player1
        self.state = GameState.PLAYING
