from .graph import *


class Road:
    def __init__(self, weight: float, parents: dict = None, finish=None):
        self._weight = weight
        self._parents = parents
        self._path = self.find_path(parents, finish)

    @staticmethod
    def find_path(parents, finish):
        path = []
        node = finish
        while node:
            path.insert(0, node)
            if parents.__contains__(node):
                node = parents[node]
            else:
                node = None
        return path

    def distance(self):
        return self._weight

    def path(self):
        return self._path

    def exists(self):
        return self._weight != float('inf')


def run(graph: WeightedGraph, start: str, finish: str) -> Road:
    """
    Finds the fastest road between two nodes in weighted and directed graph

    :param graph: graph in which road should be found
    :param start: name of the start node
    :param finish: name of the finish node
    :return: Road
    :raise NodeNotPresentException: in case of not existing start or finish nodes
    """
    costs = _initialize_node_cost_dict(graph, start)
    parents = _initialize_node_parent_dict(graph, start)
    processed = []
    node = _find_lowest_cost_not_processed_node(costs, processed)
    while node:
        cost = costs[node]
        neighbours = graph.get_neighbours_of(node)
        for n in neighbours:
            new_cost = cost + graph.get_weight_between_neighbour_nodes(node, n)
            if not costs.__contains__(n):
                return Road(float('inf'))
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = _find_lowest_cost_not_processed_node(costs, processed)
    return Road(costs[finish], parents, finish)


def _find_lowest_cost_not_processed_node(costs: dict, processed):
    not_processed_costs = {key: val for (key, val) in costs.items() if not processed.__contains__(key)}
    if len(not_processed_costs) == 0:
        return None
    return min(not_processed_costs, key=not_processed_costs.get)


def _initialize_node_cost_dict(graph, start):
    return {node: graph.get_weight_between_neighbour_nodes(start, node) for node in graph.get_all_nodes()
            if node != start}


def _initialize_node_parent_dict(graph, start):
    return {node: start for node in graph.get_all_nodes()
            if node != start and graph.get_neighbours_of(start).__contains__(node)}
