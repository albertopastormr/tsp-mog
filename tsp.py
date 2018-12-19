import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def build_graph(w_low,w_high,n):
    G = nx.Graph()
    edges = []
    weights = np.random.randint(low=w_low,high=w_high,size=int(n*(n-1)/2))
    w_ind = 0
    for v in range(1,n):
        for u in range(v+1,n):
            G.add_edge(v,u,weight=weights[w_ind])
            edges.append((v,u))
            w_ind += 1
    return G, edges, weights

def generate_tsp_path(G, origin):
    tour = []
    nodes_visited = [origin]
    actual_node = origin
    while(len(nodes_visited) < G.number_of_nodes()):
        #next_node = -1
        #next_edge = (actual_node, -1)
        min_distance = float('inf')
        for n in G.neighbors(actual_node):
            if G[actual_node][n]['weight'] < min_distance and n not in nodes_visited
             or n == origin and len(nodes_visited) == G.number_of_nodes()-1:
                min_distance = G[actual_node][n]['weight']
                next_node = n
                next_edge = (actual_node,next_node)
        nodes_visited.append(actual_node)
        tour.append(next_edge)
        actual_node = next_node
    tour.append((actual_node,origin))    
    return tour

def get_drawing_config(path, edges):
    edges_config = []
    for n in edges:
        v, u = n
        if (v,u) in path or (u,v) in path:
            edges_config.append((4,'g'))
        else:
            edges_config.append((1,'b'))
    edges_config = np.array(edges_config)
    edges_weights = list(edges_config[:,0])
    edges_colors = list(edges_config[:,1])
    edges_labels = nx.get_edge_attributes(G,'weight')
    return (edges_weights, edges_colors, edges_labels)

def random_colors(number_of_colors):
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return colors

if __name__ == "__main__":
    # complete graph construction
    n=6
    G, edges, weights = build_graph(w_low=1, w_high=12, n=n)

    # tsp solving
    path = generate_tsp_path(G,1)

    # drawing config
    edge_weights, edge_colors, edge_labels = get_drawing_config(path,edges)
    pos = nx.spring_layout(G, k=20)
    node_mapping = dict(zip(G.nodes(), [x for x in range(1,n)]))
    node_colors = random_colors(G.number_of_nodes())

    # graph plotting
    plt.figure(1,figsize=(18,12))
    nx.draw(G,pos, size=len(G.edges), labels=node_mapping, font_size=38, node_size=1350,
     node_color=node_colors, alpha=0.65, edge_color='b')
    nx.draw_networkx_edge_labels(G,pos,font_size=21 , edge_labels=edge_labels)
    plt.savefig('graph.png')
    plt.close()


    plt.figure(2,figsize=(18,12))
    nx.draw(G,pos, size=len(G.edges), labels=node_mapping, font_size=38, node_size=1350,
     node_color=node_colors, alpha=0.65, width=edge_weights, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G,pos,font_size=24 , edge_labels=edge_labels)
    plt.savefig('solution.png')

    plt.show()