import networkx as nx
import matplotlib.pyplot as plt

def visualize_matching(edges, matching):
    G = nx.Graph()
    G.add_edges_from(edges)

    pos = nx.spring_layout(G)

    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_color='black', font_size=10)

    for u, v in matching:
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '✅'}, font_color='green', font_size=8)

    plt.axis('off')
    plt.show()


def main():
    edges = [(11, 2), (3, 10), (6, 2), (8, 1), (7, 5), (6, 10), (12, 2), (14, 1), (14, 15), (5, 4),
             (2, 3), (8, 5), (6, 5), (12, 15), (9, 7), (4, 9), (15, 6), (1, 12), (5, 14), (2, 13),
             (13, 15), (13, 9), (8, 10), (15, 7), (9, 14), (1, 11), (15, 4), (13, 1), (9, 6), (10, 14)]

    matching = [(11, 2), (3, 10), (7, 5), (12, 15), (9, 7), (4, 9), (5, 14), (2, 13), (13, 15), (8, 10)]

    visualize_matching(edges, matching)


if __name__ == "__main__":
    main()