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
        self.assertTrue(road.exists())
        self.assertEqual(road.distance(), 3)
        self.assertEqual(road.path(), ['start', 'finish'])

    def test_find_way_between_three_nodes(self):
        # given
        graph = WeightedGraph('start')
        graph.add('middle', 'start', 3)
        graph.add('finish', 'middle', 2)
        # when
        road = run(graph, start='start', finish='finish')
        # then
        self.assertEqual(road.distance(), 5)
        self.assertEqual(road.path(), ['start', 'middle', 'finish'])

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
        self.assertEqual(road.path(), ['start', '1', '2', '3', '4', 'finish'])

    def test_find_shortest_way_from_many_possible_2(self):
        # given
        graph = WeightedGraph('start')

        graph.add('A', 'start', 6)
        graph.add('B', 'start', 2)

        graph.add('A', 'B', 3)

        graph.add('finish', 'A', 1)
        graph.add('finish', 'B', 5)

        # when
        road = run(graph, start='start', finish='finish')
        # then
        self.assertEqual(road.distance(), 6)
        self.assertEqual(road.path(), ['start', 'B', 'A', 'finish'])

    def test_return_infinity_if_path_do_not_exists(self):
        # given
        graph = WeightedGraph('start')
        graph.add('finish', 'start', 100)

        # when
        road = run(graph, start='finish', finish='start')
        # then
        self.assertFalse(road.exists())
        self.assertEqual(road.distance(), float('inf'))


if __name__ == '__main__':
    unittest.main()
