import pygame
from Vector import Vec2d


class SteeringManager:
    def __init__(self):
        self.steering = Vec2d(0, 0)

    def seek(self, target)
