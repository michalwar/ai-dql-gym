import numpy as np

class Environment:
    def __init__(self, grid_size, start, goal):
        self.grid_size = grid_size
        self.start = start
        self.goal = goal

    