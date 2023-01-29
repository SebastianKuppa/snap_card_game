import pygame

import engine
from models import *
from engine import *


pygame.init()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption('Snap Card Game')

if __name__ == '__main__':
    gameEngine = engine.GameEngine()

    run = True
    while run:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
