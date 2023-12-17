import copy

# graph node
class Node:
    def __init__(self, value, pos):
        self.value = value
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = float('inf')
        self.pos = pos
    
    def add_adjacency(self, node):
        self.adjacency_list.append(node)

# basic graph implementation
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        
    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2, weight=1, directed=False):
        self.edges[(node1, node2)] = weight
        node1.add_adjacency(node2)
        if not directed:
            self.edges[(node2, node1)] = weight
            node2.add_adjacency(node1)
    
    def remove_node(self, node):
        self.nodes.remove(node)
        for n in node.adjacency_list:
            if (node, n) in self.edges:
                del self.edges[(node, n)]
            if (n, node) in self.edges:
                del self.edges[(n, node)]
            if node in n.adjacency_list:
                n.adjacency_list.remove(node)
        del node
        
    def remove_edge(self, node1, node2):
        if (node1, node2) in self.edges:
            del self.edges[(node1, node2)]
        if (node2, node1) in self.edges:
            del self.edges[(node2, node1)]
        if node2 in node1.adjacency_list:
            node1.adjacency_list.remove(node2)
        if node1 in node2.adjacency_list:
            node2.adjacency_list.remove(node1)
        
    # reset the entire graph
    # make sure to call this before using another algorithm
    def reset(self):
        for node in self.nodes:
            node.visited = False
            node.predecessor = None
            node.min_distance = float('inf')

    # calculates distance from start_node to all other nodes
    # will only visit cells of which the value is in the values list
    def dijkstra(self, start_node, values=[]):
        start_node.min_distance = 0
        queue = []
        queue.append((start_node, [start_node.pos]))
        while queue:
            node, last_positions = queue.pop(0)
            if values and node.value not in values:
                continue
            for n in node.adjacency_list:
                if len(last_positions) > 2 and (last_positions[-1][0] == last_positions[-2][0] == last_positions[-3][0] == n.pos[0] or last_positions[-1][1] == last_positions[-2][1] == last_positions[-3][1] == n.pos[1]):
                    continue
                if n.min_distance > node.min_distance + n.value:
                    n.min_distance = node.min_distance + n.value
                    n.predecessor = node

                            
                    queue.append((n, [*last_positions, n.pos]))
    
    # returns shortest distance and path from start_node to end_node
    # will only visit cells of which the value is in the values list
    def shortest_path(self, start_node, end_node, values=[]):
        self.dijkstra(start_node, values)
        # not found case
        if end_node.min_distance == float('inf'):
            return -1, []
        node = end_node
        dis = node.min_distance
        visited_nodes = []
        while node:
            visited_nodes.append(node)
            node = node.predecessor
        
        return dis, visited_nodes[::-1]

# converts a 2d array into a graph
def grid_to_graph(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    graph = Graph()

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols

    # Create nodes for each cell in the grid
    for row in range(rows):
        for col in range(cols):
            node = Node(grid[row][col], [row, col])
            graph.add_node(node)

    # Add edges between neighboring cells
    for row in range(rows):
        for col in range(cols):
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor_row, neighbor_col = row + dr, col + dc
                if is_valid(neighbor_row, neighbor_col):
                    graph.add_edge(graph.nodes[row * cols + col], 
                                   graph.nodes[neighbor_row * cols + neighbor_col])

    return graph