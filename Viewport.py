# -*- coding: utf-8 -*-

import unittest
from pygame import Rect
from Vector import Vec2d


class Viewport:
    def __init__(self, screen):
        self.screen = screen
        self._rect = Rect(0, 0, 0, 0)
        self.limits = [None, None, None, None]

        # set the viewport dimensions to screen dimensions       
        self.setDimensions(self.screen.get_width(), self.screen.get_height())

        # used to centre the viewport on a gameObject's position
        self.track = None

    def setPosition(self, xOrVec, y=None):
        """ Set the position of the viewport, in global co-ords. _
        Can supply x and y, or a Vector """

        if (y is None):
            self._rect.x = xOrVec.x
            self._rect.y = xOrVec.y
        else:
            self._rect.x = xOrVec
            self._rect.y = y

    def getPosition(self):
        """ Gets the current position of the viewport, as a Vector2D """
        return Vec2d(self._rect.x, self._rect.y)

    def setDimensions(self, width=None, height=None):
        """ Sets the width and/or height of the viewport """

        if width:
            self._rect.width = width

        if height:
            self._rect.height = height

    def getRect(self):
        """ Returns a rect representing the viewport """

        return self._rect

    def inView(self, rect):
        """ Checks if any part of a rect is in the viewport """

        return self.getRect().colliderect(rect)

    def setLimit(self, index, limit):
        """ Sets the limits that the viewport can move in global co-ords """

        self.limits[index] = limit

    def checkLimits(self):
        """ Checks if the current viewport position is beyond bounds """

        pos = self.getPosition()
        if (self.limits[0]):
            if (pos.x < self.limits[0]):
                self._rect.x = self.limits[0]

        if (self.limits[1]):
            if (self._rect.topright[0] > self.limits[1]):
                self._rect.x = self.limits[1] - self._rect.width

        if (self.limits[2]):
            if (pos.y < self.limits[2]):
                self._rect.y = self.limits[2]

        if (self.limits[3]):
            if (self._rect.bottomright[1] > self.limits[3]):
                self._rect.y = self.limits[3] - self._rect.height

    def update(self):
        self.checkLimits()

    def draw(self, image, position):
        # get a vector of the local position of the sprite
        local_vec = position - self.getPosition()

        # draw the sprite's image to the local position
        self.screen.blit(image, (local_vec.x, local_vec.y))


# unit testing
class testViewport(unittest.TestCase):
    def setUp(self):
        pass

    def test_setPosition(self):
        vp = Viewport()
        vp.setPosition(101, 202)

        self.assertEqual(vp._rect.x, 101)
        self.assertEqual(vp._rect.y, 202)

        vp = Viewport()
        vec = Vec2d(303, 404)
        vp.setPosition(vec)

        self.assertEqual(vp._rect.x, 303)
        self.assertEqual(vp._rect.y, 404)

    def test_getPosition(self):
        vp = Viewport()
        vp.setPosition(101, 202)
        vec = vp.getPosition()

        self.assertEqual(vec.x, 101)
        self.assertEqual(vec.y, 202)

    def test_setDimensions(self):
        vp = Viewport()
        vp.setDimensions(102, 304)

        self.assertEqual(vp._rect.width, 102)
        self.assertEqual(vp._rect.height, 304)

    def test_setLimit(self):
        vp = Viewport()
        vp.setLimit(0, 101)
        vp.setLimit(1, 1001)
        vp.setLimit(2, 202)
        vp.setLimit(3, 2002)

        self.assertEqual(vp.limits[0], 101)
        self.assertEqual(vp.limits[1], 1001)
        self.assertEqual(vp.limits[2], 202)
        self.assertEqual(vp.limits[3], 2002)

    def test_checkLimits(self):
        vp = Viewport()
        vp.setLimit(1, 101)
        vp.setLimit(2, 1001)
        vp.setLimit(3, 202)
        vp.setLimit(4, 2002)

        vp.setPosition(50, 100)
        vp.checkLimits()
        self.assertEqual(vp._rect.x, 101)
        self.assertEqual(vp._rect.y, 202)

        vp.setPosition(1500, 2500)
        vp.checkLimits()
        self.assertEqual(vp._rect.x, 1001)
        self.assertEqual(vp._rect.y, 2002)

    def test_getRect(self):
        vp = Viewport()
        vp.setPosition(101, 202)
        vp.setDimensions(303, 404)

        rect = vp.getRect()
        self.assertEqual(rect.x, 101)
        self.assertEqual(rect.y, 202)
        self.assertEqual(rect.width, 303)
        self.assertEqual(rect.height, 404)

    def test_inView(self):
        vp = Viewport()
        vp.setPosition(0, 0)
        vp.setDimensions(1000, 1000)

        rect = Rect(100, 100, 100, 100)
        self.assertTrue(vp.inView(rect))

        rect = Rect(2000, 2000, 100, 100)
        self.assertFalse(vp.inView(rect))

if __name__ == "__main__":
    unittest.main()
