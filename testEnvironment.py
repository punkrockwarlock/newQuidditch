# -*- coding: utf-8 -*-

import pygame
import sys
import pygame.locals as locals
from Viewport import Viewport
from Vector import Vec2d


class testSprite(pygame.sprite.Sprite):
    def __init__(self, w, h):
        self.image = pygame.Surface((w, h))
        self.image.fill(locals.Color(255, 0, 0))

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
        if (event.type == locals.QUIT):
            pygame.quit()
            sys.exit()
        if (event.type == locals.KEYDOWN):
            if (event.key == locals.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if (event.key == locals.K_a):
                viewport.move(Vec2d(-20, 0))

            if (event.key == locals.K_d):
                viewport.move(Vec2d(20, 0))

            if (event.key == locals.K_s):
                viewport.move(Vec2d(0, 20))

            if (event.key == locals.K_w):
                viewport.move(Vec2d(0, -20))

            if (event.key == locals.K_RETURN):
                print viewport.getRect()

    SCREEN.fill(locals.Color(255, 255, 255))

    viewport.draw(sprite.getImage(), Vec2d(100, 100))
    viewport.draw(sprite2.getImage(), Vec2d(0, 995))
    viewport.draw(sprite3.getImage(), Vec2d(100, 200))

    viewport.update()
    pygame.display.flip()
