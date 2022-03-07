import os
import json
import numpy as np
from flask import Flask, request, render_template, jsonify
from engine.grid_graph_generator import GridGraphGenerator
from engine.hamiltonian_path import HamiltonianPath

template_directory = os.path.join(os.path.dirname(__file__), 'static')
app = Flask(
    __name__,
    template_folder = template_directory,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hamlin_path', methods = ["POST"])
def hamlin_path():
    grid = json.loads(request.form.get('grid'))

    rows = np.array(grid).shape[0]
    cols = np.array(grid).shape[1]
    black_outs = np.array(grid).reshape((1, -1))[0].tolist().count(0)
    total_nodes = rows * cols - black_outs
    
    graph_generator = GridGraphGenerator(grid)
    graph = graph_generator.get_graph()

    hamiltonian_path = HamiltonianPath(graph)
    hamlin_paths = hamiltonian_path.find_all_hamlin_paths()
    
    # Sorting out complete hamlin paths
    complete_hamlin_paths = []
    for path in hamlin_paths:
        if len(path) == total_nodes:
            complete_hamlin_paths.append(path)
    
    # Sorting out max hamlin path
    max_hamlin_path = []
    for path in hamlin_paths:
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