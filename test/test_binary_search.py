from unittest import TestCase

from algorithms.binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        # given & when
        index_found = binary_search(3, [1, 2, 3, 4])
        # then
        self.assertEqual(index_found, 2)

    def test_binary_search_finds_first_index(self):
        # given & when
        index_found = binary_search(1, [1, 2, 3, 4])
        # then
        self.assertEqual(index_found, 0)

    def test_binary_search_finds_last_index(self):
        # given & when
        index_found = binary_search(6, [1, 2, 3, 6])
        # then
        self.assertEqual(index_found, 3)
