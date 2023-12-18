import numpy as np
import random

class Environment:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []

    def _random_loc(self):
        # Get a random location
        location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

        return location

    def reset(self):
        # Initialize the empty grid as a 2D list of 0s
        self.grid = np.zeros((self.grid_size, self.grid_size))

    def add_agent(self):
        # Select a random location

        location = self._random_loc()

        # Agent is represented by a 1
        self.grid[location[0]][location[1]] = 1

        return location

    def add_goal(self):
        # Select a random location
        location = self._random_loc()

        # Get a random location until it is not occupied
        while self.grid[location[0]][location[1]] == 1:
            location = self._random_loc()

        # Goal is represented by a -1
        self.grid[location[0]][location[1]] = -1

        return location

    def render(self):
        # Convert to a list of ints to improve formatting
        grid = self.grid.astype(int).tolist()

        for row in grid:
            print(row)
        print('')

env = Environment(grid_size=5) 
env.reset()
agent_location = env.add_agent()
goal_location = env.add_goal()
env.render()


print(f'Agent Location: {agent_location}')
print(f'Goal Location: {goal_location}')





























