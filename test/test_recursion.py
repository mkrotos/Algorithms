from unittest import TestCase

from algorithms.recursion import *


class Test(TestCase):
    def test_sum_of_one_element(self):
        # given & when
        actual = sum([5])
        # then
        self.assertEqual(actual, 5)

    def test_sum(self):
        # given & when
        actual = sum([5, 2, 3])
        # then
        self.assertEqual(actual, 10)

    def test_sum_with_negative_numbers(self):
        # given & when
        actual = sum([5, 2, 3, -8])
        # then
        self.assertEqual(actual, 2)

    def test_count_elements(self):
        # given & when
        actual = count_elements_in_list([5, 2, 3, -8])
        # then
        self.assertEqual(actual, 4)

    def test_count_elements_with_one_element(self):
        # given & when
        actual = count_elements_in_list([5])
        # then
        self.assertEqual(actual, 1)

    def test_find_max_with_one_element(self):
        # given & when
        actual = find_max([5])
        # then
        self.assertEqual(actual, 5)

    def test_find_max(self):
        # given & when
        actual = find_max([5, 8, 2, 11])
        # then
        self.assertEqual(actual, 11)
