from typing import Optional
from graph_interfaces import IGraph, IVertex
from graph_impl import Graph, Vertex, Edge

def read_graph(file_path: str) -> IGraph:
    """Read the graph from the file and return the graph object"""
    graph = Graph()
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Skip the header line
        for line in lines[1:]:
            line = line.strip()
            # Skip the empty lines
            if not line:
                continue
            
            # Split by comma for CSV format
            parts = line.split(',')
            if len(parts) >= 2:
                from_name = parts[0]
                to_name = parts[1]
                
                # Find or create from vertex
                from_vertex = None
                for v in graph.get_vertices():
                    if v.get_name() == from_name:
                        from_vertex = v
                        break
                
                # If from vertex is not found then create it
                if from_vertex is None:
                    from_vertex = Vertex(from_name)
                    graph.add_vertex(from_vertex)
                
                # Find or create to vertex
                to_vertex = None
                for v in graph.get_vertices():
                    if v.get_name() == to_name:
                        to_vertex = v
                        break
                if to_vertex is None:
                    to_vertex = Vertex(to_name)
                    graph.add_vertex(to_vertex)
                
                # Create edge with the weight if available
                edge_name = f"{from_name}->{to_name}"
                weight = float(parts[3]) if len(parts) >= 4 else 1.0
                edge = Edge(edge_name, to_vertex, weight)
                from_vertex.add_edge(edge)
                graph.add_edge(edge)
    
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        
    return graph

def print_dfs(graph: IGraph, start_vertex: IVertex) -> None:
    """Print the DFS traversal of the graph starting from the start vertex"""
    # Reset all visited flags
    for v in graph.get_vertices():
        v.set_visited(False)
    print("DFS Traversal:")
    dfs_helper(start_vertex)
    print()

def dfs_helper(vertex: IVertex) -> None:
    """Print the BFS traversal of the graph starting from the start vertex"""
    vertex.set_visited(True)
    print(vertex.get_name(), end=" ")
    
    # Look at all edges
    for edge in vertex.get_edges():
        neighbor = edge.get_destination()
        if not neighbor.is_visited():
            dfs_helper(neighbor)

# Print the BFS traversal of the graph starting from the start vertex
def print_bfs(graph: IGraph, start_vertex: IVertex) -> None:
    # Reset all visited flags
    for v in graph.get_vertices():
        v.set_visited(False)
    print("BFS Traversal:")
    queue = [start_vertex]
    start_vertex.set_visited(True)
    
    # BFS loop
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.get_name(), end=",  ")
        
        for edge in  current.get_edges():
            neighbor = edge.get_destination()
            if not neighbor.is_visited():
                neighbor.set_visited(True)
                queue.append(neighbor)
    print()

# Main function to run
def main() -> None:
    graph: IGraph = read_graph("graph.txt")
    start_vertex_name: str = input("Enter the start vertex name: ")

    # Find the start vertex object
    start_vertex: Optional[IVertex] = next((v for v in graph.get_vertices() if v.get_name() == start_vertex_name), None)

    if start_vertex is None:
        print("Start vertex not found")
        return
    print_dfs(graph, start_vertex)
    print_bfs(graph, start_vertex)

if __name__ == "__main__":
    main()