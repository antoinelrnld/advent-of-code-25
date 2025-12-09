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
            new_node = Node(coord)
            for node in self.nodes:
                self.edges.append(Edge(source=new_node, dest=node, length=distance(new_node.coordinates, node.coordinates)))
            self.nodes.append(new_node)
        
    def add_node(self, node: Node):
        if node not in self.nodes:
            self.nodes.append(node)

    def add_edge(self, edge: Edge):
        if edge not in self.edges:
            self.edges.append(edge)
    
    def __repr__(self):
        return str(self.nodes)


def main():
    coordinates = read_input()
    G = Graph()
    G.build(coordinates)
    sorted_edges = sorted(G.edges, key=lambda e: e.length)

    visited_nodes = []
    for edge in sorted_edges:
        if edge.source not in visited_nodes:
            visited_nodes.append(edge.source)
        if edge.dest not in visited_nodes:
            visited_nodes.append(edge.dest)
        if len(visited_nodes) == len(G.nodes):
            return edge.dest.coordinates.x * edge.source.coordinates.x

if __name__ == '__main__':
    result = main()
    print(result)