from unittest import TestCase

from algorithms.extra.graph import *

FOURTH_NODE = 'fourth'

FIRST_NODE = 'first'
SECOND_NODE = 'second'
THIRD_NODE = 'third'
NOT_EXISTING_NODE = 'not existing node'


class Test(TestCase):

    def test_initializing(self):
        # given
        # when
        graph = WeightedGraph(FIRST_NODE)

        # then
        self.assertTrue(graph.has_node(FIRST_NODE))

    def test_add_new_node(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        # when
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        # then
        self.assertTrue(graph.has_node(SECOND_NODE))
        self.assertEqual([SECOND_NODE], graph.get_neighbours_of(FIRST_NODE))

    def test_raise_error_when_neighbour_not_present_on_adding_new_node(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        # then
        with self.assertRaises(NodeNotPresentException):
            # when
            graph.add(SECOND_NODE, NOT_EXISTING_NODE, 2)

    def test_raise_error_when_node_not_present_on_getting_neighbours(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        # then
        with self.assertRaises(NodeNotPresentException):
            # when
            graph.get_neighbours_of(NOT_EXISTING_NODE)

    def test_add_new_link_to_existing_nodes(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        graph.add(THIRD_NODE, FIRST_NODE, 3)
        graph.add(FOURTH_NODE, SECOND_NODE, 3)
        # when
        graph.add(SECOND_NODE, THIRD_NODE, 1)
        # then
        self.assertEqual([SECOND_NODE, THIRD_NODE], graph.get_neighbours_of(FIRST_NODE))
        self.assertEqual([FOURTH_NODE], graph.get_neighbours_of(SECOND_NODE))
        self.assertEqual([SECOND_NODE], graph.get_neighbours_of(THIRD_NODE))

    def test_get_lower_weight_neighbour(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        graph.add(THIRD_NODE, FIRST_NODE, 3)
        graph.add(FOURTH_NODE, FIRST_NODE, 1)
        # when
        lower_cost_node = graph.get_lower_weight_neighbour(FIRST_NODE)
        # then
        self.assertEqual(FOURTH_NODE, lower_cost_node)

    def test_raise_error_when_node_not_present_on_get_lower_weight_neighbour(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        # then
        with self.assertRaises(NodeNotPresentException):
            # when
            graph.get_lower_weight_neighbour(NOT_EXISTING_NODE)

    def test_get_weight_between_nodes(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        # when
        weight = graph.get_weight_between_neighbour_nodes(FIRST_NODE, SECOND_NODE)
        # then
        self.assertEqual(2, weight)

    def test_raise_exception_when_first_node_not_present_on_getting_weight(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        # then
        with self.assertRaises(NodeNotPresentException):
            # when
            graph.get_weight_between_neighbour_nodes(NOT_EXISTING_NODE, SECOND_NODE)

    def test_return_infinity_as_weight_on_not_existing_second_node(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        # when
        weight = graph.get_weight_between_neighbour_nodes(FIRST_NODE, SECOND_NODE)
        # then
        self.assertEqual(weight, float('inf'))

    def test_get_all_node_names(self):
        # given
        graph = WeightedGraph(FIRST_NODE)
        graph.add(SECOND_NODE, FIRST_NODE, 2)
        # when
        nodes = graph.get_all_nodes()
        # then
        self.assertEqual(nodes, [FIRST_NODE, SECOND_NODE])
