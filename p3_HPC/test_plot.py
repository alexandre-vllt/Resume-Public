import networkx as nx
import matplotlib.pyplot as plt

# Création du DAG
dag = nx.DiGraph()

# Ajout des nœuds avec leurs poids
tasks = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5,
    "E": 6,
    "F": 4,
    "G": 7,
    "H": 5,
    "I": 8
}
for task, weight in tasks.items():
    dag.add_node(task, weight=weight)

# Ajout des dépendances (arêtes)
dependencies = [
    ("A", "B"), ("A", "C"),
    ("B", "D"), ("B", "E"),
    ("C", "E"), ("C", "F"),
    ("D", "G"), ("E", "G"), ("E", "H"), ("F", "H"),
    ("G", "I"), ("H", "I")
]
dag.add_edges_from(dependencies)

# Positionnement des nœuds par niveau
pos = nx.multipartite_layout(dag, subset_key=lambda n: {"A": 0, "B": 1, "C": 1, 
                                                        "D": 2, "E": 2, "F": 2, 
                                                        "G": 3, "H": 3, 
                                                        "I": 4}[n])

# Dessin du graphe
plt.figure(figsize=(10, 6))
nx.draw_networkx_nodes(dag, pos, node_size=2000, node_color="skyblue")
nx.draw_networkx_labels(dag, pos, labels={n: f"{n} ({dag.nodes[n]['weight']})" for n in dag.nodes}, font_size=10)
nx.draw_networkx_edges(dag, pos, arrowstyle="->", arrowsize=20)
plt.title("DAG avec niveaux et poids des tâches", fontsize=14)
plt.axis("off")
plt.show()
