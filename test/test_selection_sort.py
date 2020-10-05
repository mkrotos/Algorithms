from unittest import TestCase

from algorithms.selection_sort import selection_sort


class Test(TestCase):
    def test_selection_sort(self):
        # given
        array = [3, 7, 2, 8, 3]
        # when
        actual = selection_sort(array)
        # then
        expected = [2, 3, 3, 7, 8]
        self.assertEqual(actual, expected)

    def test_list_with_negative_numbers(self):
        # given
        array = [3, -7, 2, 8, 0]
        # when
        actual = selection_sort(array)
        # then
        expected = [-7, 0, 2, 3, 8]
        self.assertEqual(actual, expected)
