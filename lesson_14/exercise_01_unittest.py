import unittest
from exercise_01 import *


class TestExercise(unittest.TestCase):

    def test_original(self):
        self.assertEqual(func(text_orig), text_orig)

    def test_reg(self):
        self.assertEqual(func(text_reg), text_orig)

    def test_punct(self):
        self.assertEqual(func(text_punc), text_orig)

    def test_all(self):
        self.assertEqual(func(text_all), text_orig)

    def test_rus(self):
        self.assertEqual(func(text_rus), text_orig)


if __name__ == '__main__':
    unittest.main(verbosity=2)
