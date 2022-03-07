from engine.grid_graph_generator import GridGraphGenerator
from engine.hamiltonian_path import HamiltonianPath

grid = [
    [1, 0, 1],
    [1, 1, 1]
]

graph = GridGraphGenerator(grid).get_graph()
hamiltonian_path = HamiltonianPath(graph)
print(hamiltonian_path.hamlin_path())