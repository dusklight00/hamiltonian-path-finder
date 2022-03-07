import numpy as np

class GridGraphGenerator():
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.rows = self.grid.shape[0]
        self.cols = self.grid.shape[1]
        
        self.n = self.rows * self.cols
        self.graph = np.zeros((self.n, self.n), dtype = int).tolist()
        self._build_graph()
        
    def get_graph(self):
        return self.graph
    
    def _build_graph(self):
        for y in range(self.rows):
            for x in range(self.cols):
                directions = self._get_all_direction_values({"x": x, "y": y})
                current_node = self._get_node_number(x, y)

                if directions["top"] == 1:
                    top_node = self._get_node_number(x, y - 1)
                    self._add_edge(current_node, top_node)

                if directions["right"] == 1:
                    right_node = self._get_node_number(x + 1, y)
                    self._add_edge(current_node, right_node)

                if directions["bottom"] == 1:
                    bottom_node = self._get_node_number(x, y + 1)
                    self._add_edge(current_node, bottom_node)

                if directions["left"] == 1:
                    left_node = self._get_node_number(x - 1, y)
                    self._add_edge(current_node, left_node)

    def _get_all_direction_values(self, index):
        x = index["x"]
        y = index["y"]

        # If the node value is 0 it will connect to other nodes
        if self.grid[y][x] == 0:
            return {"top": 0, "right": 0, "bottom": 0, "left": 0}

        result = {
            "top": self.grid[y - 1][x] if y - 1 >= 0 else 0,
            "right": self.grid[y][x + 1] if x + 1 < self.cols else 0,
            "bottom": self.grid[y + 1][x] if y + 1 < self.rows else 0,
            "left": self.grid[y][x - 1] if x - 1 >= 0 else 0
        }

        return result

    def _get_node_number(self, x, y):
        return y * self.cols + x
    
    def _add_edge(self, v1, v2):
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1
    
    def _remove_edge(self, v1, v2):
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0