from unittest import TestCase

from algorithms.extra.graph import WeightedGraph


class Test(TestCase):

    def test_initializing(self):
        # given
        # when
        graph = WeightedGraph('first')

        # then
        self.assertTrue(graph.has_node('first'))

    def test_add_new_node(self):
        # given
        graph = WeightedGraph('first')
        # when
        graph.add('second', 'first', 2)
        # then
        self.assertTrue(graph.has_node('second'))
        self.assertEqual(['second'], graph.getNeighboursOf('first'))