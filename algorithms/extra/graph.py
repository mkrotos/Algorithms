class WeightedGraph:
    """
    Object oriented implementation of weighted and directed graph
    """

    def __init__(self, initial_node):
        self._nodes = {initial_node: _Node(initial_node)}

    def add(self, new_node, neighbour_of, weight):
        if self.has_node(neighbour_of):
            self._nodes[neighbour_of].add_neighbour(new_node, weight)
            if not self.has_node(new_node):
                self._nodes[new_node] = _Node(new_node)
        else:
            raise NodeNotPresentException(neighbour_of)

    def has_node(self, name: str):
        return self._nodes.__contains__(name)

    def get_neighbours_of(self, node):
        if self.has_node(node):
            return self._nodes[node].get_neighbours()
        raise NodeNotPresentException(node)

    def get_lower_weight_neighbour(self, node):
        if self.has_node(node):
            return self._nodes[node].get_lower_weight_neighbour()
        raise NodeNotPresentException(node)

    def get_weight_between_neighbour_nodes(self, node, neighbour):
        if self.has_node(node):
            return self._nodes[node].get_weight_to_neighbour(neighbour)
        raise NodeNotPresentException(node)

    def get_all_nodes(self):
        return [node for node in self._nodes.keys()]


class _Node:
    def __init__(self, name):
        self._name = name
        self._neighbours = {}

    def add_neighbour(self, node, weight: int):
        self._neighbours[node] = weight

    def get_neighbours(self):
        return [neighbour for neighbour in self._neighbours.keys()]

    def get_lower_weight_neighbour(self):
        first_neighbour = self._neighbours.popitem()
        name = first_neighbour[0]
        lower_weight = first_neighbour[1]
        for neighbour in self._neighbours.keys():
            if self._neighbours[neighbour] < lower_weight:
                name = neighbour
                lower_weight = self._neighbours[neighbour]
        return name

    def get_weight_to_neighbour(self, neighbour):
        if self.has_neighbour(neighbour):
            return self._neighbours[neighbour]
        return float('inf')

    def has_neighbour(self, neighbour):
        return self._neighbours.__contains__(neighbour)


class NodeNotPresentException(Exception):
    def __init__(self, node_name):
        self.message = f'Node [{node_name}] do not exists'
        super().__init__(self.message)
