from dataclasses import dataclass
from math import sqrt


@dataclass
class Coordinates:
    x: int
    y: int
    z: int


@dataclass
class Node:
    coordinates: Coordinates
    neighbors: list["Node"]


@dataclass
class Edge:
    source: Node
    dest: Node
    length: int

def read_input():
    with open('input.txt') as f:
        coordinates = []
        for box in f:
            if box.strip() != "":
                x, y, z = box.split(',')
                coordinates.append(Coordinates(int(x), int(y), int(z)))
        return coordinates


def distance(c1: Coordinates, c2: Coordinates):
    return sqrt((c2.x - c1.x)**2 + (c2.y - c1.y)**2 + (c2.z - c1.z)**2)


class Graph:
    def __init__(self):
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
    
    def build(self, coords: list[Coordinates]):
        for coord in coords:
            new_node = Node(coord, [])
            for node in self.nodes:
                node.neighbors.append(new_node)
                new_node.neighbors.append(node)
                self.edges.append(Edge(source=new_node, dest=node, length=distance(new_node.coordinates, node.coordinates)))
            self.nodes.append(new_node)
    
    def add_node(self, node: Node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, edge: Edge):
        if edge not in self.edges:
            self.edges.append(edge)
            if edge.dest not in edge.source.neighbors:
                edge.source.neighbors.append(edge.dest)
            if edge.source not in edge.dest.neighbors:
                edge.dest.neighbors.append(edge.source)
    
    def __repr__(self):
        return str(self.nodes)


def get_all_connected_nodes(node: Node, visited: list[Node]):
    visited.append(node)
    for n in node.neighbors:
        if not n in visited:
            get_all_connected_nodes(n, visited)


def main():
    coordinates = read_input()
    G = Graph()
    G.build(coordinates)
    sorted_edges = sorted(G.edges, key=lambda e: e.length)

    for node in G.nodes:
        node.neighbors = []

    G2 = Graph()
    for edge in sorted_edges[:1000]:
        G2.add_node(edge.source)
        G2.add_node(edge.dest)
        G2.add_edge(Edge(edge.source, edge.dest, edge.length))
    
    isolated_networks = []
    visited_nodes = []
    for node in G2.nodes:
        network = []
        if node not in visited_nodes:
            get_all_connected_nodes(node, network)
            isolated_networks.append(network)
            visited_nodes.extend(network)
    longests = sorted(isolated_networks, key=lambda x: len(x), reverse=True)
    
    result = len(longests[0]) * len(longests[1]) * len(longests[2])

    return result



if __name__ == '__main__':
    result = main()
    print(result)