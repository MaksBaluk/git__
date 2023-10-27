import unittest
from file import plus


class plusTest(unittest.TestCase):

    def test_plus(self):
        res = plus(2, 3)
        self.assertEqual(res, 5)

    def test_error(self):
        res = plus(3, 3)
        self.assertNotEqual(res, 7)
