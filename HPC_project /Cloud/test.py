import boto3
import json
import sys
import os
import io
sys.path.append('/var/task/networkx')
import networkx as nx
# import matplotlib.pyplot as plt
#from scipy.interpolate import griddata
# from mpl_toolkits.mplot3d import Axes3D
from ordonnancement import hlfet_scheduler
from jsong import generate_graph
from schedule import run_experiments

def handler(event, context):
    bucket='central-supelec-data-group3'

    s3_client=boto3.client('s3')

    graph=generate_graph(1000000)
    graph_json=json.dumps(graph, indent=2)

    fname='input_data/graphe1M.json'
    s3_client.put_object(Bucket=bucket, Key=fname, Body=graph_json)
    response=s3_client.get_object(Bucket=bucket, Key=fname)

    data=json.load(response['Body'])
    schedule=hlfet_scheduler(data, num_cores=100)

    iterations=[4, 6, 8]+[5*i for i in range(2,20)]+[100*j for j in range(1,10)]+[1000*k for k in range(1,10)]+[10000*l for l in range(1,10)]+[100000*m for m in range(1,11)]+[10000000]
    results=run_experiments(iterations, 100)

    # fig1, ax1 = plt.subplots()
    # plot_execution_times(results, ax1)
    # buf1 = io.BytesIO()
    # fig1.savefig(buf1, format='png')
    # buf1.seek(0)
    # s3_client.put_object(Bucket=bucket, Key='output_data/execution_times.png', Body=buf1, ContentType='image/png')
    # plt.close(fig1)

    # fig2 = plt.figure()
    # ax2 = fig2.add_subplot(111, projection='3d')
    # plot_3d_execution_surface(results, ax2)
    # buf2 = io.BytesIO()
    # fig2.savefig(buf2, format='png')
    # buf2.seek(0)
    # s3_client.put_object(Bucket=bucket, Key='output_data/3d_surface.png', Body=buf2, ContentType='image/png')
    # plt.close(fig2)

    cores_range = [3, 5, 10, 50, 100, 1000, 10000, 50000]
    execution_times = []
    makespans = []

    for cores in cores_range:
        import time
        start = time.time()
        sched = hlfet_scheduler(graph, num_cores=cores)
        exec_time = time.time() - start
        execution_times.append(exec_time)

        end_times = [t["start"] + t["duration"] for t in sched["tasks"]]
        makespans.append(max(end_times) if end_times else 0)

    # fig3, ax3 = plt.subplots()
    # ax3.plot(cores_range, execution_times, marker='o', label='Temps de calcul')
    # ax3.plot(cores_range, makespans, marker='x', label='Makespan')
    # ax3.set_xlabel("Nombre de coeurs")
    # ax3.set_ylabel("Secondes")
    # ax3.set_title("Évolution du temps de calcul et du makespan")
    # ax3.legend()
    # ax3.grid(True)

    # buf3 = io.BytesIO()
    # fig3.savefig(buf3, format='png')
    # buf3.seek(0)
    # s3_client.put_object(Bucket=bucket, Key='output_data/performance_vs_cores.png', Body=buf3, ContentType='image/png')
    # plt.close(fig3)


    return {"schedule" : schedule, "makespan" : makespans, "endtime": end_times}