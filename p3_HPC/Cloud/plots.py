import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

def plot_execution_times(results):
    num_tasks = [res["num_tasks"] for res in results]
    exec_times = [res["execution_time"] for res in results]
    
    plt.figure(figsize=(10, 5))
    plt.scatter(num_tasks, exec_times, color='b', label='Temps d\'exécution')
    plt.plot(sorted(num_tasks), sorted(exec_times), linestyle='--', color='r')
    plt.xlabel("Nombre de tâches")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps d'exécution en fonction du nombre de tâches")
    plt.legend()
    plt.grid()
    plt.show()

def plot_3d_execution_surface(results):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    num_tasks = np.array([res["num_tasks"] for res in results])
    exec_times = np.array([res["execution_time"] for res in results])
    dependency_coeffs = np.array([res["dependency_coefficient"] for res in results])
    
    # Création d'une grille pour interpoler les données
    grid_x, grid_y = np.meshgrid(
        np.linspace(num_tasks.min(), num_tasks.max(), 30),
        np.linspace(dependency_coeffs.min(), dependency_coeffs.max(), 30)
    )
    grid_z = griddata((num_tasks, dependency_coeffs), exec_times, (grid_x, grid_y), method='cubic')
    
    ax.plot_surface(grid_x, grid_y, grid_z, cmap='viridis', alpha=0.7)
    ax.scatter(num_tasks, dependency_coeffs, exec_times, c=exec_times, cmap='viridis', marker='o')
    ax.set_xlabel("Nombre de tâches")
    ax.set_ylabel("Coefficient de dépendance")
    ax.set_zlabel("Temps d'exécution (s)")
    ax.set_title("Surface 3D du temps d'exécution en fonction de la dépendance et du nombre de tâches")
    
    plt.show()