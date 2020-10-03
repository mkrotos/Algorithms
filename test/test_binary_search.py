from unittest import TestCase

from algorithms.binary_search import binary_search


class Test(TestCase):
    def test_binary_search(self):
        # given & when
        index_found = binary_search([1, 2, 3, 4], 3)
        # then
        self.assertEqual(index_found, 2)

    def test_binary_search_finds_first_index(self):
        # given & when
        index_found = binary_search([1, 2, 3, 4], 1)
        # then
        self.assertEqual(index_found, 0)

    def test_binary_search_finds_last_index(self):
        # given & when
        index_found = binary_search([1, 2, 3, 6], 6)
        # then
        self.assertEqual(index_found, 3)

    def test_return_none_if_target_not_present(self):
        # given & when
        index_found = binary_search([1, 2, 3, 6], 5)
        # then
        self.assertEqual(index_found, None)


