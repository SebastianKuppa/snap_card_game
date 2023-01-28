from enum import Enum
import pygame
from models import *


class GameState(Enum):
    PLAYING = 0
    SNAPPING = 1
    ENDED = 2


class GameEngine:
    result = {}

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

    def winRound(self, player):
        self.state = GameState.SNAPPING
        player.hand.extend(self.pile.popAll())
        self.pile.clear()

    def play(self, key):
        if key is None:
            return

        if self.state == GameState.ENDED:
            return

        if key == self.current_player.flipKey:
            self.pile.add(self.current_player.play())
            self.switchPlayer()

        snapCaller = None
        nonSnapCaller = None
        isSnap = self.pile.isSnap()

        if key == self.player1.snapKey:
            snapCaller = self.player1
            nonSnapCaller = self.player2
        elif key == self.player2.snapKey:
            snapCaller = self.player2
            nonSnapCaller = self.player1

        if isSnap and snapCaller:
            self.result = {
                "winner": snapCaller,
                "isSnap": True,
                "snapCaller": snapCaller
            }
            self.winRound(snapCaller)

        elif not isSnap and snapCaller:
            self.result = {
                "winner": nonSnapCaller,
                "isSnap": False,
                "snapCaller": snapCaller
            }
            self.winRound(nonSnapCaller)
