markdown# Graph Traversal Assignment

## Author
Connor Everetts

## Description
This project implements a directed graph data structure and two fundamental graph traversal algorithms: Breadth-First Search (BFS) and Depth-First Search (DFS). The implementation uses an adjacency list representation for efficient graph operations.

The graph represents cities in Oregon connected by highways, with each edge containing distance information.

## Implementation Details
- **Graph representation**: Adjacency list
- **Data structures**: Custom classes implementing provided interfaces
- **Traversal algorithms**: DFS (recursive) and BFS (queue-based)
- **File format**: CSV with headers (source, destination, highway, distance)

## How to Run
1. Ensure you have Python 3 installed
2. Place all files in the same directory
3. Run the program:
python program.py
4. Enter a starting vertex when prompted (e.g., "Portland")

## File Format
The graph.txt file is in CSV format:
source,destination,highway,distance
Portland,Salem,I-5,47
...

## Sample Output

### DFS Traversal (starting from Portland)
DFS Traversal:
Portland Salem Eugene Corvallis Newport Tillamook Seaside Astoria Florence Coos_Bay Roseburg Medford Ashland Crater_Lake Bend Redmond Madras The_Dalles Hood_River Pendleton Ontario Burns

### BFS Traversal (starting from Portland)
BFS Traversal:
Portland Salem Astoria Hood_River Newport Eugene Corvallis Seaside The_Dalles Tillamook Florence Bend Crater_Lake Roseburg Pendleton Madras Coos_Bay Redmond Burns Medford Ontario Ashland

## Design Decisions
- Used adjacency list representation for O(m+n) space complexity
- DFS implemented recursively for simplicity and clarity
- BFS implemented iteratively using a list as a queue
- File parser skips the CSV header and handles comma-separated values
- Graph stores edge weights but traversal algorithms don't use them (preparation for future shortest-path algorithms)
- Vertex visited flags are reset before each traversal to allow multiple searches

## Files Included
- `graph_interfaces.py` - Interface definitions (provided)
- `graph_impl.py` - Implementation of Graph, Vertex, and Edge classes
- `program.py` - Main program with file parsing and traversal algorithms
- `graph.txt` - Oregon cities graph data in CSV format
- `README.md` - This file