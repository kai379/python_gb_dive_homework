import unittest
from Rectangle import Rectangle
from functools import total_ordering


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.side_b = 10
        self.rec_1 = Rectangle(5, 10)
        self.rec_2 = Rectangle(5)

    def test_init_side_b_have(self):
        self.assertEqual(self.rec_1.side_b, self.side_b)

    def test_init_side_b_None(self):
        self.assertIsNot(self.rec_2.side_b, None)

    def test_area(self):
        self.assertEqual(self.rec_1.area(), 50)
        self.assertEqual(self.rec_2.area(), 25)

    def test_perimetr(self):
        self.assertEqual(self.rec_1.perimeter(), 30)
        self.assertEqual(self.rec_2.perimeter(), 20)

    def test_gt(self):
        self.assertGreater(self.rec_1, self.rec_2)


if __name__ == '__main__':
    unittest.main()
