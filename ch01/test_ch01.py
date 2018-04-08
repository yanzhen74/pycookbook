import unittest
from e26 import get_record_pos
from collatz_puzzle import get_collatz_list


class TestE26(unittest.TestCase):
    def test_e26(self):
        # rl = ch01.get_record_pos(5, 3, 18)
        self.assertEqual(get_record_pos(5, 3, 18), (2, 1, 3))
        self.assertEqual(get_record_pos(5, 3, 16), (2, 1, 1))
        self.assertEqual(get_record_pos(5, 3, 17), (2, 1, 2))
        self.assertEqual(get_record_pos(5, 3, 19), (2, 2, 1))
        self.assertEqual(get_record_pos(5, 3, 30), (2, 5, 3))
        self.assertEqual(get_record_pos(5, 3, 33), (3, 1, 3))
        self.assertEqual(get_record_pos(5, 3, 31), (3, 1, 1))
        self.assertEqual(get_record_pos(5, 3, 15), (1, 5, 3))
        self.assertEqual(get_record_pos(5, 3, 1), (1, 1, 1))

    def test_collatz(self):
        r = [3]
        get_collatz_list(3, r)
        self.assertEqual(len(r), 8)