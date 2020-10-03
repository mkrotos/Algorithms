from unittest import TestCase

from algorithms.binary_search_recursive import binary_search_recursive


class Test(TestCase):

    def test_binary_search_recursive(self):
        # given & when
        index_found = binary_search_recursive([1, 2, 3, 4], 3)
        # then
        self.assertEqual(index_found, 2)

    def test_binary_search_finds_first_index_recursive(self):
        # given & when
        index_found = binary_search_recursive([1, 2, 3, 4], 1)
        # then
        self.assertEqual(index_found, 0)

    def test_binary_search_finds_last_index_recursive(self):
        # given & when
        index_found = binary_search_recursive([1, 2, 3, 6], 6)
        # then
        self.assertEqual(index_found, 3)

    def test_return_none_if_target_not_present_recursive(self):
        # given & when
        index_found = binary_search_recursive([1, 2, 3, 6], 5)
        # then
        self.assertEqual(index_found, None)
