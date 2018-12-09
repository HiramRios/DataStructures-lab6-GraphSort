'''
Created on Dec 1, 2018

@author: hiramrios
'''


import heapq

# Stores a collection of vertex sets, which collectively store all vertices in a
# graph. Each vertex is in only one set in the collection.




class Vertex:
    def __init__(self, label):
        self.label = label
        
class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}
        
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
        
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)
        
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)        
    
    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None
    
class EdgeWeight:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
    
    # Only edge weights are used in the comparisons that follow
    
    def __eq__(self, other):
        return self.weight == other.weight
    
    def __ge__(self, other):
        return self.weight >= other.weight
    
    def __gt__(self, other):
        return self.weight > other.weight

    def __le__(self, other):
        return self.weight <= other.weight
    
    def __lt__(self, other):
        return self.weight < other.weight
    
    def __ne__(self, other):
        return self.weight != other.weight
 
 
 
# Stores a collection of vertex sets, which collectively store all vertices in a
# graph. Each vertex is in only one set in the collection.
class VertexSetCollection:
    def __init__(self, all_vertices):
        self.vertex_map = dict()
        for vertex in all_vertices:
            vertex_set = set()
            vertex_set.add(vertex)
            self.vertex_map[vertex] = vertex_set

    def __len__(self):
        return len(self.vertex_map)

    # Gets the set containing the specified vertex
    def get_set(self, vertex):
        return self.vertex_map[vertex]

    # Merges two vertex sets into one
    def merge(self, vertex_set1, vertex_set2):
        # First create the union
        merged = vertex_set1.union(vertex_set2)
        # Now remap all vertices in the merged set
        for vertex in merged:
            self.vertex_map[vertex] = merged 
        
        
        

def get_incoming_edge_count(edge_list, vertex):
    count = 0
    for (from_vertex, to_vertex) in edge_list:
        if to_vertex is vertex:
            count = count + 1
    return count

def topological_sort(graph):
    result_list = []

    # make list of vertices with no incoming edges.
    no_incoming = []
    for vertex in graph.adjacency_list.keys():
        if get_incoming_edge_count(graph.edge_weights.keys(), vertex) == 0:
            no_incoming.append(vertex)
    
    # remaining_edges starts with all edges in the graph.
    # A set is used for its efficient remove() method.
    remaining_edges = set(graph.edge_weights.keys())
    while len(no_incoming) != 0:
        # select the next vertex for the final result.
        current_vertex = no_incoming.pop()
        result_list.append(current_vertex)
        outgoing_edges = []

        # remove current_vertex's outgoing edges from remaining_edges.
        for to_vertex in graph.adjacency_list[current_vertex]:
            outgoing_edge = (current_vertex, to_vertex)
            if outgoing_edge in remaining_edges:
                outgoing_edges.append(outgoing_edge)
                remaining_edges.remove(outgoing_edge)
        
        # see if removing the outgoing edges creates any new vertices
        # with no incoming edges.
        for (from_vertex, to_vertex) in outgoing_edges:
            in_count = get_incoming_edge_count(remaining_edges, to_vertex)
            if in_count == 0:
                no_incoming.append(to_vertex)
    
    return result_list








def minimum_spanning_tree(graph):
    # edge_list starts as a list of all edges from the graph
    edge_list = []
    for edge in graph.edge_weights:
        edge_weight = EdgeWeight(edge[0], edge[1], graph.edge_weights[edge])
        edge_list.append(edge_weight)
    # Turn edge_list into a priority queue (min heap)
    heapq.heapify(edge_list)

    # Initialize the collection of vertex sets
    vertex_sets = VertexSetCollection(graph.adjacency_list)

    # result_list is initially an empty list
    result_list = []

    while len(vertex_sets) > 1 and len(edge_list) > 0:
        # Remove edge with minimum weight from edge_list
        next_edge = heapq.heappop(edge_list)
        
        # set1 = set in vertex_sets containing next_edge's 'from' vertex
        set1 = vertex_sets.get_set(next_edge.from_vertex)
        # set2 = set in vertex_sets containing next_edge's 'to' vertex
        set2 = vertex_sets.get_set(next_edge.to_vertex)
        
        # If the 2 sets are distinct, then merge
        if set1 is not set2:
            # Add next_edge to result_list
            result_list.append(next_edge)
            # Merge the two sets within the collection
            vertex_sets.merge(set1, set2)

    return result_list










