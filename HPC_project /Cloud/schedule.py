from ordonnancement import hlfet_scheduler

import json
import random
import networkx as nx
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
from time import time
# import numpy as np
# from scipy.interpolate import griddata
from jsong import generate_graph

# def generate_random_graph(num_tasks, max_duration=20, max_dependencies=3):
#     tasks = []
#     for i in range(1, num_tasks + 1):
#         task_id = f"task{i}"
#         duration = random.randint(1, max_duration)
#         dependencies = random.sample(
#             [f"task{j}" for j in range(1, i)], k=min(len(range(1, i)), max_dependencies)
#         ) if i > 1 else []
#         tasks.append({"id": task_id, "duration": duration, "dependencies": dependencies})
    
#     return {"graph_id": f"graph_{num_tasks}", "tasks": tasks}

def compute_dependency_coefficient(graph):
    num_nodes = len(graph["tasks"])
    num_edges = sum(len(task["dependencies"]) for task in graph["tasks"])
    return num_edges / num_nodes if num_nodes > 0 else 0

def run_experiments(iterations, num_cores):
    results = []
    
    for i in range(iterations):
        graph=generate_graph(i)

        dependency_coefficient = compute_dependency_coefficient(graph)
        
        start_time = time()
        schedule, _ = hlfet_scheduler(graph, num_cores)
        exec_time = time() - start_time
        
        results.append({
            "num_tasks": i, 
            "execution_time": exec_time,
            "dependency_coefficient": dependency_coefficient
        })
    
    return results

# def plot_execution_times(results):
#     num_tasks = [res["num_tasks"] for res in results]
#     exec_times = [res["execution_time"] for res in results]
    
#     plt.figure(figsize=(10, 5))
#     plt.scatter(num_tasks, exec_times, color='b', label='Temps d\'exécution')
#     plt.plot(sorted(num_tasks), sorted(exec_times), linestyle='--', color='r')
#     plt.xlabel("Nombre de tâches")
#     plt.ylabel("Temps d'exécution (s)")
#     plt.title("Temps d'exécution en fonction du nombre de tâches")
#     plt.legend()
#     plt.grid()
#     plt.show()

# def plot_3d_execution_surface(results):
#     fig = plt.figure(figsize=(10, 7))
#     ax = fig.add_subplot(111, projection='3d')
    
#     num_tasks = np.array([res["num_tasks"] for res in results])
#     exec_times = np.array([res["execution_time"] for res in results])
#     dependency_coeffs = np.array([res["dependency_coefficient"] for res in results])
    
#     # Création d'une grille pour interpoler les données
#     grid_x, grid_y = np.meshgrid(
#         np.linspace(num_tasks.min(), num_tasks.max(), 30),
#         np.linspace(dependency_coeffs.min(), dependency_coeffs.max(), 30)
#     )
#     grid_z = griddata((num_tasks, dependency_coeffs), exec_times, (grid_x, grid_y), method='cubic')
    
#     ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis', alpha=0.7)
#     ax.scatter(num_tasks, dependency_coeffs, exec_times, c=exec_times, cmap='viridis', marker='o')
#     ax.set_xlabel("Nombre de tâches")
#     ax.set_ylabel("Coefficient de dépendance")
#     ax.set_zlabel("Temps d'exécution (s)")
#     ax.set_title("Surface 3D du temps d'exécution en fonction de la dépendance et du nombre de tâches")
    
#     plt.show()

# Configuration des expériences
# iterations = 500
# min_tasks = 5
# max_tasks = 5000
# num_cores = 100

# # Lancer les expériences et afficher les résultats
# experiment_results = run_experiments(iterations, min_tasks, max_tasks, num_cores)
# print(json.dumps(experiment_results, indent=4))

# # Tracer les graphiques
# plot_execution_times(experiment_results)
# plot_3d_execution_surface(experiment_results)