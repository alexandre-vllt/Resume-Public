import json
import random
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import time
import numpy as np
from scipy.interpolate import griddata



def generate_random_graph(num_tasks, max_duration=20, max_dependencies=3):
    tasks = []
    for i in range(1, num_tasks + 1):
        task_id = f"task{i}"
        duration = random.randint(1, max_duration)
        dependencies = random.sample(
            [f"task{j}" for j in range(1, i)], k=min(len(range(1, i)), max_dependencies)
        ) if i > 1 else []
        tasks.append({"id": task_id, "duration": duration, "dependencies": dependencies})
    
    return {"graph_id": f"graph_{num_tasks}", "tasks": tasks}

DAG = generate_random_graph(30, 20, 5)