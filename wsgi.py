from flask import Flask, request, render_template, jsonify
import numpy as np
from engine.grid_graph_generator import GridGraphGenerator
from engine.hamiltonian_path import HamiltonianPath

app = Flask(__name__)

@app.route('/get_hamlin_path')
def hamlin_path():
    grid = [
        [1, 1, 1],
        [1, 1, 1]
    ]
    rows = np.array(grid).shape[0]
    cols = np.array(grid).shape[1]
    total_nodes = rows * cols

    graph_generator = GridGraphGenerator(grid)
    graph = graph_generator.get_graph()

    hamiltonian_path = HamiltonianPath(graph)
    hamlin_paths = hamiltonian_path.hamlin_path()
    
    # Sorting out complete hamlin paths
    complete_hamlin_paths = []
    for path in hamlin_paths:
        if len(path) == total_nodes:
            complete_hamlin_paths.append(path)
    
    # Sorting out max hamlin path
    max_hamlin_path = []
    for path in complete_hamlin_paths:
        if len(path) > len(max_hamlin_path):
            max_hamlin_path = path
    
    result = {
        "complete_hamlin_paths": complete_hamlin_paths,
        "max_hamlin_path": max_hamlin_path,
        "hamlin_paths": hamlin_paths
    }

    return jsonify(result)


    

    

if __name__ == '__main__':
    app.run(debug = True)