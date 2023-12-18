import numpy as np
import random

class Environment:
    def __init__(self, grid_size, render_on):
        self.grid_size = grid_size
        self.grid = []
        self.render_on = render_on
        self.agent_location = None
        self.goal_location = None

    def _random_loc(self):
        # Get a random location
        location = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))

        return location

    def reset(self):
        # Initialize the empty grid as a 2D list of 0s
        self.grid = np.zeros((self.grid_size, self.grid_size))

        # Add the agent and goal
        self.agent_location = self.add_agent()
        self.goal_location = self.add_goal()

        if self.render_on:
            self.render()

        # Return the current state

        return self.get_state()

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

    def get_state(self):
        # Return the current state
        state = self.grid.flatten()
        return state

env = Environment(grid_size=5, render_on=True) 
env.reset()


print(f'Agent Location: {agent_location}')
print(f'Goal Location: {goal_location}')





























