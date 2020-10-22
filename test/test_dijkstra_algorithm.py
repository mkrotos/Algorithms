import unittest

from algorithms.extra.dijkstra_algorithm import *
from algorithms.extra.graph import *


class MyTestCase(unittest.TestCase):
    def test_find_way_between_two_nodes(self):
        # given
        graph = WeightedGraph('start')
        graph.add('finish', 'start', 3)
        # when
        road = run(graph, start='start', finish='finish')
        # then
        self.assertEqual(road.distance(), 3)

    def test_find_way_between_three_nodes(self):
        # given
        graph = WeightedGraph('start')
        graph.add('middle', 'start', 3)
        graph.add('finish', 'middle', 2)
        # when
        road = run(graph, start='start', finish='finish')
        # then
        self.assertEqual(road.distance(), 5)

    def test_find_shortest_way_from_many_possible(self):
        # given
        graph = WeightedGraph('start')

        graph.add('trap', 'start', 1)
        graph.add('finish', 'trap', 100)

        graph.add('1', 'start', 10)
        graph.add('2', '1', 1)
        graph.add('3', '2', 1)
        graph.add('4', '3', 1)
        graph.add('finish', '4', 1)

        # when
        road = run(graph, start='start', finish='finish')
        # then
        self.assertEqual(road.distance(), 14)


if __name__ == '__main__':
    unittest.main()
