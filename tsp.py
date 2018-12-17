import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

def build_graph(edges,weights):
    G = nx.Graph()
    for i, e in enumerate(edges):
        G.add_edge(*e, weight=weights[i])
    return G

def doub(edges):
    ret = []
    for e in edges:
        v, u = e
        ret.append((v,u))
        ret.append((u,v))
    return ret

def generate_tsp_path(G, origin):
    tour = []
    nodes_visited = [origin]
    actual_node = origin
    while(len(nodes_visited) < G.number_of_nodes()):
        #next_node = -1
        #next_edge = (actual_node, -1)
        min_distance = float('inf')
        for n in G.neighbors(actual_node):
            if G[actual_node][n]['weight'] < min_distance and n not in nodes_visited or n == origin and len(nodes_visited) == G.number_of_nodes()-1:
                min_distance = G[actual_node][n]['weight']
                next_node = n
                next_edge = (actual_node,next_node)
        nodes_visited.append(actual_node)
        tour.append(next_edge)
        actual_node = next_node
    
    return tour
    #return [(1,2),(2,3),(3,4),(4,5)] # example

def get_drawing_config(path, edges):
    edges_config = []
    for n in edges:
        v, u = n
        if (v,u) in path or (u,v) in path:
            edges_config.append((4,'g'))
        else:
            edges_config.append((1,'b'))
    edges_config = np.array(edges_config)
    #edges_config = np.array([(1,'b') for n in edges])
    edges_weights = list(edges_config[:,0])
    edges_colors = list(edges_config[:,1])
    edges_labels = nx.get_edge_attributes(G,'weight')
    return (edges_weights, edges_colors, edges_labels)

def random_colors(number_of_colors):
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    return colors

if __name__ == "__main__":
    n=12

    # graph construction
    #edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5),(5,6),(4,6)] # example
    edges = [(i,x) for x in range(i+1,n) for i in range(1,n)]
    weights = np.random.randint(low=1,high=12,size=len(edges))

    G = build_graph(edges,weights)

    # tsp solving
    path = generate_tsp_path(G,1)
    print(path)
    # drawing config
    edge_weights, edge_colors, edge_labels = get_drawing_config(path,edges)
    pos = nx.spring_layout(G, k=G.number_of_nodes()/len(edges))
    node_mapping = dict(zip(G.nodes(),"abcdefg")) # example
    node_colors = random_colors(G.number_of_nodes())

    # graph plotting
    plt.figure(1,figsize=(18,12))
    nx.draw(G,pos, size=len(G.edges), labels=node_mapping, font_size=32, node_size=750,
     node_color=node_colors, alpha=0.65, edge_color='b')
    nx.draw_networkx_edge_labels(G,pos,font_size=21 , edge_labels=edge_labels)
    plt.savefig('graph.png')
    plt.close()


    plt.figure(2,figsize=(18,12))
    nx.draw(G,pos, size=len(G.edges), labels=node_mapping, font_size=32, node_size=750,
     node_color=node_colors, alpha=0.65, width=edge_weights, edge_color=edge_colors)
    nx.draw_networkx_edge_labels(G,pos,font_size=21 , edge_labels=edge_labels)
    plt.savefig('solution.png')

    plt.show()