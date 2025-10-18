from graph_interfaces import IEdge, IGraph, IVertex
from typing import List

class Graph(IGraph):
    def __init__(self) -> None:
        self._vertices: List[IVertex] = []
        self._edges: List[IEdge] = []

    def get_vertices(self) -> List[IVertex]:
        return self._vertices
    
    def get_edges(self) -> List[IEdge]:
        return self._edges
    
    def add_vertex(self, vertex: IVertex) -> None:
        self._vertices.append(vertex)
    
    def remove_vertex(self, vertex_name: str) -> None:
        for vertex in self._vertices:
            if vertex.get_name() == vertex_name:
                self._vertices.remove(vertex)
                return
    
    def add_edge(self, edge: IEdge) -> None:
        self._edges.append(edge)
    
    def remove_edge(self, edge_name: str) -> None:
        for edge in self._edges:
            if edge.get_name() == edge_name:
                self._edges.remove(edge)
                return
            
class Vertex(IVertex):
    def __init__(self, name: str) -> None:
        self._name: str = name
        self._edges: List[IEdge] = []
        self._visited: bool = False

    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
    
    def add_edge(self, edge: IEdge) -> None:
        self._edges.append(edge)
    
    def remove_edge(self, edge_name: str) -> None:
        for edge in self._edges:
            if edge.get_name() == edge_name:
                self._edges.remove(edge)
                return
    
    def get_edges(self) -> List[IEdge]:
        return self._edges
    
    def set_visited(self, visited: bool) -> None:
        self._visited = visited
    
    def is_visited(self) -> bool:
        return self._visited


class Edge(IEdge):
    def __init__(self, name: str, destination: IVertex, weight: float =  1.0) -> None:
        self._name: str = name
        self._destination: IVertex = destination
        self._weight: float = weight

    def get_name(self) -> str:
         return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
    
    def get_destination(self) -> IVertex:
        return self._destination
    
    def get_weight(self) -> float:
        return self._weight
    
    def set_weight(self, weight: float) -> None:
        self._weight = weight