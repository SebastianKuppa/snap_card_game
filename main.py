import pygame

import engine
from models import *
from engine import *


pygame.init()
clock = pygame.time.Clock()
bounds = (1024, 768)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption('Snap Card Game')

card_back = pygame.image.load('images/BACK.png')
card_back = pygame.transform.scale(card_back, (int(238*0.8), int(332*0.8)))


def renderGame(window):
    window.fill((15, 0, 169))
    font = pygame.font.SysFont('comicsans', 60, bold=True)

    window.blit(card_back, (100, 200))
    window.blit(card_back, (700, 200))

    text = font.render(str(len(gameEngine.player1.hand)) + 'cards', True, (255, 255, 255))
    window.blit(text, (100, 500))
    text = font.render(str(len(gameEngine.player2.hand)) + 'cards', True, (255, 255, 255))
    window.blit(text, (700, 500))

    top_card = gameEngine.pile.peek()
    if top_card is not None:
        window.blit(top_card.image, (400, 200))

    if gameEngine.state == GameState.PLAYING:
        text = font.render(gameEngine.current_player.name + ' to flip', True, (255, 255, 255))
        window.blit(text, (20, 50))

    if gameEngine.state == GameState.SNAPPING:
        result = gameEngine.result
        if result['isSnap'] is True:
            message = "Winning Snap! by " + result['winner'].name
        else:
            message = "False Snap! by " + result['snapCaller'].name + '. ' + result['winner'].name + ' wins!'
        text = font.render(message, True, (255, 255, 255))
        window.blit(text, (20, 50))

    if gameEngine.state == GameState.ENDED:
        result = gameEngine.result
        message = "Game Over! " + result["winner"].name + " wins the game."
        text = font.render(message, True, (255, 255, 255))
        window.blit(text, (20, 50))


if __name__ == '__main__':
    gameEngine = engine.GameEngine()

    run = True
    while run:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                key = event.key

        gameEngine.play(key)
        renderGame(window)
        pygame.display.update()
        clock.tick()

        if gameEngine.state == GameState.SNAPPING:
            pygame.time.delay(3000)
            gameEngine.state = GameState.PLAYING