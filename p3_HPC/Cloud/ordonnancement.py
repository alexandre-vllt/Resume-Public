import json
import networkx as nx

def hlfet_scheduler(input_data, num_cores):
    # Parse input data
    tasks = {task["id"]: {
        "duration": task["duration"],
        "dependencies": task["dependencies"]
    } for task in input_data["tasks"]}

    # Create DAG
    dag = nx.DiGraph()
    
    # Add nodes and edges
    for task_id, task_data in tasks.items():
        dag.add_node(task_id, duration=task_data["duration"])
        for dep in task_data["dependencies"]:
            dag.add_edge(dep, task_id)

    # Calculate task levels
    levels = {}
    for node in nx.topological_sort(dag):
        if not list(dag.predecessors(node)):
            levels[node] = 0
        else:
            levels[node] = max(levels[pred] for pred in dag.predecessors(node)) + 1

    # Sort tasks by level and duration
    sorted_tasks = sorted(tasks.keys(), 
                        key=lambda x: (-levels[x], -tasks[x]["duration"]), 
                        reverse=False)

    # Initialize scheduling
    schedule = {f"core_{i}": [] for i in range(num_cores)}
    core_availability = {i: 0 for i in range(num_cores)}

    # Schedule tasks
    for task in sorted_tasks:
        # Calculate earliest start time based on dependencies
        est = 0
        for pred in tasks[task]["dependencies"]:
            pred_finish = max([core_availability[i] - schedule[f"core_{i}"][-1][1] 
                            for i in range(num_cores) if any(t[0] == pred for t in schedule[f"core_{i}"])], default=0)
            est = max(est, pred_finish)

        # Find best core
        best_core = min(core_availability, 
                    key=lambda c: max(core_availability[c], est) + tasks[task]["duration"])
        
        start_time = max(core_availability[best_core], est)
        end_time = start_time + tasks[task]["duration"]
        
        # Update schedule and core availability
        schedule[f"core_{best_core}"].append((task, start_time))
        core_availability[best_core] = end_time

    # Format output
    formatted_schedule = {}
    for core, tasks in schedule.items():
        formatted_schedule[core] = sorted([
            {"task": t[0], "start_time": t[1]} 
            for t in tasks
        ], key=lambda x: x["start_time"])

    return formatted_schedule

# Exemple d'utilisation
input_json = {
    "graph_id": "graph_example",
    "tasks": [
        {"id": "task1", "duration": 10, "memory": 512, "dependencies": []},
        {"id": "task2", "duration": 15, "memory": 1024, "dependencies": ["task1"]},
        {"id": "task3", "duration": 5, "memory": 256, "dependencies": ["task1"]},
        {"id": "task4", "duration": 5, "memory": 256, "dependencies": ["task2"]},
        {"id": "task5", "duration": 15, "memory": 256, "dependencies": ["task1", "task4"]},
        {"id": "task6", "duration": 25, "memory": 256, "dependencies": ["task4"]},
        {"id": "task7", "duration": 7, "memory": 256, "dependencies": ["task1"]},
        {"id": "task8", "duration": 8, "memory": 256, "dependencies": ["task1"]},
        {"id": "task9", "duration": 9, "memory": 256, "dependencies": ["task1"]}
    ]
}

output = hlfet_scheduler(input_json, num_cores=4)
print(json.dumps(output, indent=2))