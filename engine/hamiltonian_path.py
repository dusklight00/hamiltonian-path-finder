class HamiltonianPath:
    def __init__(self, graph):
        self.graph = graph

    def find_all_hamlin_paths(self):
        possible_paths = []
        for i in range(len(self.graph)):
            possible_path = self.hamlin_path([i])
            possible_paths += possible_path
            if len(possible_path) == 0:
                continue
            if len(possible_path[0]) == 1:
                continue
            break

        return possible_paths

    def hamlin_path(self, path = [0]):
        next_paths = self._next_path(path)

        if next_paths is None:
            return [path]

        possible_paths = []
        for next_path in next_paths:
            new_path = path + [next_path[-1]]
            new_possible_paths = self.hamlin_path(new_path)
            possible_paths += new_possible_paths
            
        return possible_paths

    def _next_path(self, path):
        if len(path) == len(self.graph):
            return None
        
        next_paths = []
        for i in range(len(self.graph)):
            if i not in path and self.graph[path[-1]][i] == 1:
                next_paths.append((path[-1], i))
        
        if not len(next_paths) == 0:
            return next_paths

        return None