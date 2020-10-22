from .graph import *


class Road:
    def __init__(self, weight):
        self._weight = weight

    def distance(self):
        return self._weight


def _find_lowest_cost_not_processed_node(costs: dict, processed):
    not_processed_costs = {key: val for (key, val) in costs.items() if not processed.__contains__(key)}
    print(not_processed_costs)
    if len(not_processed_costs) is 0:
        return None
    return min(not_processed_costs, key=not_processed_costs.get)


def run(graph: WeightedGraph, start: str, finish: str) -> Road:
    """
    Finds the fastest road between two nodes.

    :param graph: graph in which road should be found
    :param start: name of the start node
    :param finish: name of the finish node
    :return: Road
    :raise NodeNotPresentException: in case of not existing start or finish nodes
    """
    costs = {node: graph.get_weight_between_neighbour_nodes(start, node) for node in graph.get_all_nodes() if
             node != start}
    parents = {node: start for node in graph.get_all_nodes() if
               node != start and graph.get_neighbours_of(start).__contains__(node)}
    print(costs)
    processed = []
    node = _find_lowest_cost_not_processed_node(costs, processed)
    while node is not None:
        print(node)
        cost = costs[node]
        neighbours = graph.get_neighbours_of(node)
        for n in neighbours:
            new_cost = cost + graph.get_weight_between_neighbour_nodes(node, n)
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = _find_lowest_cost_not_processed_node(costs, processed)
    return Road(costs[finish])
