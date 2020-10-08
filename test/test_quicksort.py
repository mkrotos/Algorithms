from unittest import TestCase

from algorithms.quicksort import quicksort


class Test(TestCase):
    def test_single_element_list(self):
        # given & when
        actual = quicksort([1])
        # then
        self.assertEqual([1], actual)

    def test_sort_list(self):
        # given & when
        actual = quicksort([1, 8, 4, 9])
        # then
        self.assertEqual([1, 4, 8, 9], actual)

    def test_sort_empty_list(self):
        # given & when
        actual = quicksort([])
        # then
        self.assertEqual([], actual)
