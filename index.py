from engine.grid_graph_generator import GridGraphGenerator
from engine.hamiltonian_path import HamiltonianPath

grid = [
    [1, 1, 1],
    [1, 1, 1]
]

graph_generator = GridGraphGenerator(grid)
graph = graph_generator.get_graph()

hamiltonian_path = HamiltonianPath(graph)
path = hamiltonian_path.hamlin_path()
print(path)