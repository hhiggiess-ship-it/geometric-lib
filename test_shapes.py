import math
import unittest

import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):

    def test_area_from_readme(self):
        # Проверка примера из README: rectangle.area(4, 8) -> 32
        self.assertEqual(rectangle.area(4, 8), 32)

    def test_area_zero(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_perimeter_from_readme(self):
        # Проверка примера из README: rectangle.perimeter(3, 9) -> 24
        self.assertEqual(rectangle.perimeter(3, 9), 24)

    def test_perimeter_zero(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)


class SquareTestCase(unittest.TestCase):

    def test_area_from_readme(self):
        # Проверка примера из README: square.area(5) -> 25
        self.assertEqual(square.area(5), 25)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter_from_readme(self):
        # Проверка примера из README: square.perimeter(12) -> 48
        self.assertEqual(square.perimeter(12), 48)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)


class CircleTestCase(unittest.TestCase):

    def test_area_from_readme(self):
        # Проверка примера из README: circle.area(10) -> pi * 100
        self.assertAlmostEqual(circle.area(10), math.pi * 100, places=5)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter_from_readme(self):
        # Проверка примера из README: circle.perimeter(5) -> 2 * pi * 5
        self.assertAlmostEqual(circle.perimeter(5), 2 * math.pi * 5, places=5)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)


class TriangleTestCase(unittest.TestCase):

    def test_area_from_readme(self):
        # Проверка примера из README: triangle.area(8, 5) -> 20.0
        self.assertEqual(triangle.area(8, 5), 20.0)

    def test_area_zero(self):
        self.assertEqual(triangle.area(0, 5), 0.0)

    def test_perimeter_from_readme(self):
        # Проверка примера из README: triangle.perimeter(5, 5, 6) -> 16
        self.assertEqual(triangle.perimeter(5, 5, 6), 16)

    def test_perimeter_zero(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)