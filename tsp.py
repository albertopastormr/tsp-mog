import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def build_graph(edges):
    G = nx.Graph()
    for e in edges:
        G.add_edge(*e)
    return G

def generate_tsp_path(G):
    return [(1,2),(2,3),(3,4),(4,5)] # example

def get_drawing_config(path, edges):
    edges_config = [(4,'g') if n in path else (1,'b') for n in edges]
    edges_config = np.array(edges_config)
    edges_weights = list(edges_config[:,0])
    edges_colors = list(edges_config[:,1])
    return (edges_weights, edges_colors)

def random_colors(number_of_colors):
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return colors

if __name__ == "__main__":
    edges = [(1,2),(2,3),(3,1),(3,4),(4,5),(4,6),(6,7)] # example
    G = build_graph(edges)

    path = generate_tsp_path(G)

    nodes_mapping = dict(zip(G.nodes(),"abcdefg")) # example
    edges_weights, edges_colors = get_drawing_config(path,edges)

    # graph plotting
    nx.draw(G, size=len(G.edges), labels=nodes_mapping, font_size=32, node_color=random_colors(G.number_of_nodes()), alpha=0.3, width=edges_weights, edge_color=edges_colors)
    plt.show()