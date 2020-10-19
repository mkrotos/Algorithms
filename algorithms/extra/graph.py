class WeightedGraph:
    """
    Object oriented implementation of weighted and directed graph
    """

    def __init__(self, initial_node):
        self.nodes = {initial_node: Node(initial_node)}

    def add(self, new_node, neighbour_of, weight):
        if self.has_node(neighbour_of):
            self.nodes[neighbour_of].add_neighbour(new_node, weight)
            if not self.has_node(new_node):
                self.nodes[new_node] = Node(new_node)
        else:
            raise NodeNotPresentException(neighbour_of)

    def has_node(self, name: str):
        return self.nodes.__contains__(name)

    def get_neighbours_of(self, node):
        if self.has_node(node):
            return self.nodes[node].get_neighbours()
        raise NodeNotPresentException(node)

    def get_lower_weight_neighbour(self, node):
        if self.has_node(node):
            return self.nodes[node].get_lower_weight_neighbour()
        raise NodeNotPresentException(node)

    def get_weight_between_nodes(self, node, neighbour):
        if self.has_node(node):
            return self.nodes[node].get_weight_to_neighbour(neighbour)
        raise NodeNotPresentException(node)


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = {}

    def add_neighbour(self, node, weight: int):
        self.neighbours[node] = weight

    def get_neighbours(self):
        return [neighbour for neighbour in self.neighbours.keys()]

    def get_lower_weight_neighbour(self):
        first_neighbour = self.neighbours.popitem()
        name = first_neighbour[0]
        lower_weight = first_neighbour[1]
        for neighbour in self.neighbours.keys():
            if self.neighbours[neighbour] < lower_weight:
                name = neighbour
                lower_weight = self.neighbours[neighbour]
        return name

    def get_weight_to_neighbour(self, neighbour):
        if self.has_neighbour(neighbour):
            return self.neighbours[neighbour]
        return None

    def has_neighbour(self, neighbour):
        return self.neighbours.__contains__(neighbour)


class NodeNotPresentException(Exception):
    def __init__(self, node_name):
        self.message = f'Node [{node_name}] do not exists'
        super().__init__(self.message)
