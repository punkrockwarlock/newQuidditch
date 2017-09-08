import pygame
import sys
from pygame.locals import *
from Viewport import Viewport
from Vector import Vec2d


class testSprite(pygame.sprite.Sprite):
    def __init__(self, w, h):
        self.image = pygame.Surface((w, h))
        self.image.fill(Color(255, 0, 0))

    def getImage(self):
        return self.image

# globals
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
viewport = Viewport(SCREEN)
viewport.setLimit(3, 1000)
sprite = testSprite(100, 100)
sprite2 = testSprite(600, 2)
sprite3 = testSprite(5, 800)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if (event.type == QUIT):
            pygame.quit()
            sys.exit()
        if (event.type == KEYDOWN):
            if (event.key == K_a):
                viewport.setPosition(viewport.getPosition() + Vec2d(-20, 0))

            if (event.key == K_d):
                viewport.setPosition(viewport.getPosition() + Vec2d(20, 0))

            if (event.key == K_s):
                viewport.setPosition(viewport.getPosition() + Vec2d(0, 20))

            if (event.key == K_w):
                viewport.setPosition(viewport.getPosition() + Vec2d(0, -20))

            if (event.key == K_RETURN):
                print viewport.getRect()

    SCREEN.fill(Color(255, 255, 255))

    viewport.draw(sprite.getImage(), Vec2d(100, 100))
    viewport.draw(sprite2.getImage(), Vec2d(0, 995))
    viewport.draw(sprite3.getImage(), Vec2d(100, 200))

    viewport.update()
    pygame.display.flip()
