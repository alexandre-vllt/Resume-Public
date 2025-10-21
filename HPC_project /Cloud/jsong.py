import json
import random

def generate_graph(num_tasks):
    graph = {
        "graph_id": "generated_graph",
        "tasks": []
    }

    for i in range(1, num_tasks + 1):
        task_id = f"task{i}"
        duration = random.randint(5, 30) 
        memory = random.choice([256, 512, 1024])  
        dependencies = []

        if i > 1:  # La première tâche n'a pas de dépendances
            num_dependencies = random.randint(0, min(3, i-1))  # Max 3 dépendances
            dependencies = random.sample([f"task{j}" for j in range(1, i)], num_dependencies)

        graph["tasks"].append({
            "id": task_id,
            "duration": duration,
            "memory": memory,
            "dependencies": dependencies
        })

    return graph

#num_tasks=int(input("nombre de tâches : "))
# generated_graph = generate_graph(num_tasks)
# with open("generated_graph.json", "w") as f:
#     json.dump(generated_graph, f, indent=2)

# print(f"Graphe avec {num_tasks} tâches généré dans 'generated_graph.json'.")
