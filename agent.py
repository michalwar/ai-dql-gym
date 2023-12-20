from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import numpy as np  

class Agent:
    def __init__(self, grid_size, epsilon, epsilon_decay, epsilon_end, learning_rate, hidden_size):
        # Hyperparameters
        self.grid_size = grid_size
        self.hidden_size = 128
        self.learning_rate = 0.01
        self.epsilon = 1.0
        self.epsilon_decay = 0.998
        self.epsilon_end = 0.01
        

        # Agent model
        self.model = self.build_model()

    def build_model(self):
        # Create a sequential model with 3 layers
        model = Sequential([
            # Input layer expects a flattened grid, hence the grid_size**2
            Dense(self.hidden_size, activation='relu', input_shape=(self.grid_size**2,)),
            Dense(self.hidden_size/2, activation='relu'),
            # Output layer with 4 units for the possible actions (up, down, left, right)
            Dense(4, activation='linear')
        ])

        # Compile the model with an optimizer and a loss function
        model.compile(optimizer='adam', loss='mse')

        return model

    def get_action(self, state):
        
        # rand() returns a random value between 0 and 1
        if np.random.rand() <= self.epsilon:
            # Exploration: random action
            action = np.random.randint(0, 4)
        else:
            # Add an extra dimension to the state to create a batch with one dimension
            state = np.expand_dims(state, axis=0)

            # Use the model to predict the q-values for each action for the given state
            q_values = self.model.predict(state, verbose=0)

            # Select and return the action with the highest q-value
            action = np.argmax(q_values[0]) # [0] because the model returns a batch of predictions and we only want the first one

        # Decay the epsilon value to reduce exploration over time
        if self.epsilon > self.epsilon_end:
            self.epsilon *= self.epsilon_decay

        return action