'''
Created on Dec 4, 2018

@author: hiramrios
'''
from Graph import topological_sort, minimum_spanning_tree, Graph, Vertex, EdgeWeight, VertexSetCollection


g = Graph()



vertex_A = Vertex('A')
vertex_B = Vertex('B')
vertex_C = Vertex('C')
vertex_D = Vertex('D')
vertex_E = Vertex('E')
vertex_F = Vertex('F')
vertex_G = Vertex('G')
    
g.add_vertex(vertex_A)
g.add_vertex(vertex_B)
g.add_vertex(vertex_C)
g.add_vertex(vertex_D)
g.add_vertex(vertex_E)
g.add_vertex(vertex_F)
g.add_vertex(vertex_G)
g.add_directed_edge(vertex_A, vertex_B)
g.add_directed_edge(vertex_A, vertex_C)
g.add_directed_edge(vertex_B, vertex_F)
g.add_directed_edge(vertex_C, vertex_D)
g.add_directed_edge(vertex_D, vertex_F)
g.add_directed_edge(vertex_E, vertex_F)
g.add_directed_edge(vertex_E, vertex_G)
g.add_directed_edge(vertex_F, vertex_G)
    

result_list = topological_sort(g)
    
    # display sorted list
first = True
for vertex in result_list:
    if first:
        first = False
    else:
        print(' -> '),
    print(vertex.label),
print(" ")


graph1 = Graph()

vertex_names = ["A", "B", "C", "D", "E", "F", "G", "H"]








for vertex_name in vertex_names:
    graph1.add_vertex(Vertex(vertex_name))

# Add edges
graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("B"), 15)
graph1.add_undirected_edge(graph1.get_vertex("A"), graph1.get_vertex("D"), 6)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("C"), 9)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("D"), 12)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("G"), 14)
graph1.add_undirected_edge(graph1.get_vertex("B"), graph1.get_vertex("H"), 10)
graph1.add_undirected_edge(graph1.get_vertex("C"), graph1.get_vertex("E"), 16)
graph1.add_undirected_edge(graph1.get_vertex("D"), graph1.get_vertex("E"), 8)
graph1.add_undirected_edge(graph1.get_vertex("E"), graph1.get_vertex("F"), 20)
   
tree_edges = minimum_spanning_tree(graph1)


print("Edges in minimum spanning tree (graph 1):")
for edge in tree_edges:
    print(edge.from_vertex.label + " to " + edge.to_vertex.label),
    print(", weight = " + str(edge.weight))


result_list = topological_sort(graph1)




