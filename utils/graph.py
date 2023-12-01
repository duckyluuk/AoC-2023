# graph node
class Node:
    def __init__(self, value):
        self.value = value
        self.visited = False
        self.predecessor = None
        self.adjacency_list = []
        self.min_distance = float('inf')
    
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
    
    # breadth first search
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        visited_nodes = []
        start_node.visited = True
        while queue:
            node = queue.pop(0)
            # do some check on this node
            # (example: skip nodes that are false)
            if node.value == False:
                continue
            visited_nodes.append(node)
            for n in node.adjacency_list:
                if not n.visited:
                    n.visited = True
                    queue.append(n)
        
        return visited_nodes
    
    # depth first search
    def dfs(self, start_node):
        stack = []
        stack.append(start_node)
        visited_nodes = []
        start_node.visited = True
        while stack:
            node = stack.pop()
            # do some check on this node 
            # (example: skip nodes that are false)
            if node.value == False:
                continue
            visited_nodes.append(node)
            for n in node.adjacency_list:
                if not n.visited:
                    n.visited = True
                    stack.append(n)
        
        return visited_nodes
        

    # calculates distance from start_node to all other nodes
    # will only visit cells of which the value is in the values list
    def dijkstra(self, start_node, values=[]):
        start_node.min_distance = 0
        queue = []
        queue.append(start_node)
        while queue:
            node = queue.pop(0)
            if values and node.value not in values:
                continue
            for n in node.adjacency_list:
                if n.min_distance > node.min_distance + self.edges[(node, n)]:
                    n.min_distance = node.min_distance + self.edges[(node, n)]
                    n.predecessor = node
                    queue.append(n)
    
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
    
    # returns the largest area of connected nodes and which nodes are in it
    # will only visit cells of which the value is in the values list
    def largest_area(self, values=[]):
        max_area = 0
        max_nodes = []
        for node in self.nodes:
            if values and node.value not in values:
                continue
            if not node.visited:
                visited_nodes = self.dfs(node)
                print(visited_nodes)
                if len(visited_nodes) > max_area:
                    max_area = len(visited_nodes)
                    max_nodes = visited_nodes
        
        return max_area, max_nodes
    
    # returns the lowest node that is an ancestor of both node1 and node2
    def lowest_common_ancestor(self, node1, node2):
        visited_nodes1 = self.dfs(node1)
        visited_nodes2 = self.dfs(node2)
        common_nodes = list(set(visited_nodes1) & set(visited_nodes2))
        return common_nodes[-1]

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
            node = Node(grid[row][col])
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

# convert 3d grid to graph
def grid_to_graph_3d(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    depth = len(grid[0][0]) if cols > 0 else 0
    graph = Graph()

    def is_valid(row, col, d):
        return 0 <= row < rows and 0 <= col < cols and 0 <= d < depth

    # Create nodes for each cell in the grid
    for row in range(rows):
        for col in range(cols):
            for d in range(depth):
                node = Node(grid[row][col][d])
                graph.add_node(node)

    # Add edges between neighboring cells
    for row in range(rows):
        for col in range(cols):
            for d in range(depth):
                for dr, dc, dd in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                    neighbor_row, neighbor_col, neighbor_d = row + dr, col + dc, d + dd
                    if is_valid(neighbor_row, neighbor_col, neighbor_d):
                        graph.add_edge(graph.nodes[row * cols * depth + col * depth + d], 
                                       graph.nodes[neighbor_row * cols * depth + neighbor_col * depth + neighbor_d])

    return graph


# converts a dictionary tree into a graph
# example input:                becomes
# dictionary = {                    a
#     "a": {                       / \
#         "b": {                  b   e
#             "c": {},           / \
#             "d": {}           c   d
#         },
#         "e": {}
#     }
# }
def dict_tree_to_graph(dictionary, directed=False):
    graph = Graph()
    def convert(dictionary, parent):
        for key in dictionary:
            print(key)
            node = Node(key)
            graph.add_node(node)
            if parent:
                graph.add_edge(parent, node, directed=directed)
            convert(dictionary[key], node)
    convert(dictionary, None)
    return graph


# converts a dictionary of connections into a graph
# example input:                becomes
# dictionary = {                    a
#     "a": ["b", "e"],             / \
#     "b": ["c", "d"],            b   e
#     "e": []                    / \
# }                             c   d
def dict_connections_to_graph(dictionary, directed=False):
    nodes = {}
    graph = Graph()
    for key in dictionary:
        node = Node(key)
        graph.add_node(node)
        nodes[key] = node
        
    for key in dictionary:
        for connection in dictionary[key]:
            graph.add_edge(nodes[key], nodes[connection], directed=directed)
            
    return graph


# converts a dictionary of connections into a weighted graph
# example input:                becomes
# dictionary = {
#    "a": {"b": 1, "e": 2},      a
#    "b": {"c": 3, "d": 4},   1 / \ 2
#    "e": {}                   b   e
# }                         3 / \ 4
#                            c   d
def dict_connections_to_weighted_graph(dictionary, directed=False):
    nodes = {}
    graph = Graph()
    for key in dictionary:
        node = Node(key)
        graph.add_node(node)
        nodes[key] = node
        
    for key in dictionary:
        for connection in dictionary[key]:
            graph.add_edge(nodes[key], nodes[connection], dictionary[key][connection], directed=directed)
            
    return graph

# pathfinding function implementing the graph class
# inputs a 2d map, outputs shortest distance (edge weights)
# and list of nodes in the path
def pathfind(map_2d):
    graph = grid_to_graph(map_2d)
    start_node = graph.nodes[0]
    end_node = graph.nodes[-1]
    distance, path = graph.shortest_path(start_node, end_node, [0])
    return distance, path

# finds largest area inside a 2d grid
# for example, the largest area of 1s in the grid
def find_largest_area(map_2d):
    graph = grid_to_graph(map_2d)
    return graph.largest_area([0])




# converts a list into a binary tree graph
# example input:                becomes
# arr = [1,2,3,4,5,6,7]           1
#                                / \
#                               2   3
#                              / \ / \
#                             4  5 6  7
def list_to_binary_tree_graph(arr):
    graph = Graph()
    for i in range(len(arr)):
        node = Node(arr[i])
        graph.add_node(node)
        if i > 0:
            if i % 2 == 0:
                graph.add_edge(graph.nodes[i // 2 - 1], node, directed=True)
            else:
                graph.add_edge(graph.nodes[i // 2], node, directed=True)
    return graph