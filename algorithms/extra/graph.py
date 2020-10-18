class WeightedGraph:
    """
    Object oriented implementation of weighted directed graph
    """

    def __init__(self, initial_node):
        self.nodes = {}
        self.nodes[initial_node] = Node(initial_node)

    def add(self, new_node, neighbour_of, weight):
        if self.has_node(neighbour_of):
            self.nodes[new_node] = Node(new_node)
            self.nodes[neighbour_of].add_neighbour(new_node, weight)
        else:
            raise NeighbourNotPresentException()

    def has_node(self, name: str):
        return self.nodes.__contains__(name)


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, node, weight: int):
        self.neighbours.append(NeighbourNode(node, weight))


class NeighbourNode:
    def __init__(self, node: Node, weight: int):
        self.node = node
        self.weight = weight


class NeighbourNotPresentException(Exception):
    pass
