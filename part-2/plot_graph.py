import networkx as nx
import matplotlib.pyplot as plt


def plot_metro_network():

    G = nx.Graph()

    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'G'),
        ('E', 'H'), ('E', 'I'),
        ('F', 'J'),
        ('I', 'J')
    ]

    G.add_edges_from(edges)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color='lightblue',
        edge_color='gray',
        node_size=2000,
        font_size=12)

    plt.title('Mapa de la Red de Metro')
    plt.show()


plot_metro_network()
