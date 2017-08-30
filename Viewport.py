import unittest
from enum import Enum
from pygame import Rect
from Vector import Vec2d


class LimitIndex(Enum):
    X_MIN = 0
    X_MAX = 1
    Y_MIN = 2
    Y_MAX = 3


class Viewport:
    def __init__(self):
        self._rect = Rect(0, 0, 0, 0)
        self.limits = [None, None, None, None]

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

    def setLimit(self, index, limit):
        """ Sets the limits that the viewport can move in global co-ords

            'index' can be any of enum:
            LimitIndex.X_MIN
            LimitIndex.X_MAX
            LimitIndex.Y_MIN
            LimitIndex.Y_MAX"""

        self.limits[index.value] = limit

    def checkLimits(self):
        """ Checks if the current viewport position is beyond bounds """

        pos = self.getPosition()
        if (self.limits[LimitIndex.X_MIN.value]):
            if (pos.x < self.limits[LimitIndex.X_MIN.value]):
                self._rect.x = self.limits[LimitIndex.X_MIN.value]

        if (self.limits[LimitIndex.X_MAX.value]):
            if (self._rect.topright[0] > self.limits[LimitIndex.X_MAX.value]):
                self._rect.x = self.limits[LimitIndex.X_MAX.value]

        if (self.limits[LimitIndex.Y_MIN.value]):
            if (pos.y < self.limits[LimitIndex.Y_MIN.value]):
                self._rect.y = self.limits[LimitIndex.Y_MIN.value]

        if (self.limits[LimitIndex.Y_MAX.value]):
            if (self._rect.bottomright[1] < self.limits[LimitIndex.Y_MAX.value]):
                self._rect.y = self.limits[LimitIndex.Y_MAX.value]


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
        vp.setLimit(LimitIndex.X_MIN, 101)
        vp.setLimit(LimitIndex.X_MAX, 1001)
        vp.setLimit(LimitIndex.Y_MIN, 202)
        vp.setLimit(LimitIndex.Y_MAX, 2002)

        self.assertEqual(vp.limits[LimitIndex.X_MIN.value], 101)
        self.assertEqual(vp.limits[LimitIndex.X_MAX.value], 1001)
        self.assertEqual(vp.limits[LimitIndex.Y_MIN.value], 202)
        self.assertEqual(vp.limits[LimitIndex.Y_MAX.value], 2002)

    def test_checkLimits(self):
        vp = Viewport()
        vp.setLimit(LimitIndex.X_MIN, 101)
        vp.setLimit(LimitIndex.X_MAX, 1001)
        vp.setLimit(LimitIndex.Y_MIN, 202)
        vp.setLimit(LimitIndex.Y_MAX, 2002)

        vp.setPosition(50, 100)
        vp.checkLimits()
        self.assertEqual(vp._rect.x, 101)
        self.assertEqual(vp._rect.y, 202)

        vp.setPosition(1500, 2500)
        vp.checkLimits()
        self.assertEqual(vp._rect.x, 1001)
        self.assertEqual(vp._rect.y, 2002)

if __name__ == "__main__":
    unittest.main()
