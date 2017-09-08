import pygame.locals as locals
import unittest
from Vector import Vec2d


class GameEntity:
    def __init__(self):
        self._rect = locals.Rect(0, 0, 0, 0)

    def setPosition(self, xOrVec, y=None):
        """ Set the position of the game entity, in global co-ords. _
        Can supply x and y, or a Vector """

        if (y is None):
            self._rect.x = xOrVec.x
            self._rect.y = xOrVec.y
        else:
            self._rect.x = xOrVec
            self._rect.y = y

    def move(self, xOrVec, y=None):
        """ Moves the position of the game entity by the given offset. _
        Can supply x and y, or a Vector """

        if (y is None):
            self.setPosition(self.getPosition() + xOrVec)
        else:
            self._rect.x += xOrVec
            self._rect.y += y

    def getPosition(self):
        """ Gets the current position of the game entity, as a Vector2D """
        return Vec2d(self._rect.x, self._rect.y)

    def setDimensions(self, width=None, height=None):
        """ Sets the width and/or height of the game entity """

        if width:
            self._rect.width = width

        if height:
            self._rect.height = height

    def getRect(self):
        """ Returns a rect representing the game entity """

        return self._rect


# unit testing
class testGameEntity(unittest.TestCase):
    def setUp(self):
        pass

    def test_setPosition(self):
        vp = GameEntity()
        vp.setPosition(101, 202)

        self.assertEqual(vp._rect.x, 101)
        self.assertEqual(vp._rect.y, 202)

        vp = GameEntity()
        vec = Vec2d(303, 404)
        vp.setPosition(vec)

        self.assertEqual(vp._rect.x, 303)
        self.assertEqual(vp._rect.y, 404)

    def test_getPosition(self):
        vp = GameEntity()
        vp.setPosition(101, 202)
        vec = vp.getPosition()

        self.assertEqual(vec.x, 101)
        self.assertEqual(vec.y, 202)

    def test_setDimensions(self):
        vp = GameEntity()
        vp.setDimensions(102, 304)

        self.assertEqual(vp._rect.width, 102)
        self.assertEqual(vp._rect.height, 304)

    def test_getRect(self):
        vp = GameEntity()
        vp.setPosition(101, 202)
        vp.setDimensions(303, 404)

        rect = vp.getRect()
        self.assertEqual(rect.x, 101)
        self.assertEqual(rect.y, 202)
        self.assertEqual(rect.width, 303)
        self.assertEqual(rect.height, 404)

    def test_move(self):
        vp = GameEntity()
        vp.setPosition(0, 0)
        vp.setDimensions(1000, 1000)

        vp.move(10, 10)
        self.assertEqual(vp.getPosition(), Vec2d(10, 10))

if __name__ == "__main__":
    unittest.main()
