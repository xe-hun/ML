import random
import numpy as np


class UCB:
  """
  This class implements the UCB (Upper Confidence Bound) algorithm for reinforcement learning.
  """

  def __init__(self, numActions, numStates, c = 1):
    """
    Initializes the UCB agent.

    Args:
        num_actions: The number of actions the agent can take.
    """
    self.numberOfActions = numActions
    self.numberOfStates = numStates
    self.c = c # Exploration parameter (controls the balance between exploitation and exploration)
    self.rewards = np.zeros((numStates, numActions), dtype=int)  # Sum of rewards for each action
    self.actionSelected = np.zeros((numStates, numActions), dtype=int) 
    self.stateVisit = np.zeros(numStates, dtype=int)# Number of times each action has been selected
   

  def chooseAction(self, state):
    """
    Chooses an action based on the UCB formula.

    Args:
        t: The current time step (used for calculating the confidence bound).

    Returns:
        The index of the chosen action.
    """
    

    
    
    
    if np.all(self.actionSelected[state]) == False or self.stateVisit[state] == 0:  # Initial exploration - choose random action if no selections yet
      return np.random.choice(self.numberOfActions)

    # Calculate average reward for each action (handling division by zero)
    average_rewards = self.rewards[state] / np.maximum(self.actionSelected[state], 1)

    # Calculate the UCB value for each action
    ucbValues = average_rewards + self.c * np.sqrt(np.log(self.stateVisit[state]) / self.actionSelected[state])

    # Choose the action with the highest UCB value
    return self.randomTieBreakArgmax(ucbValues.tolist())

  def update(self, state, action, reward):
    """
    Updates the agent's knowledge based on the chosen action and received reward.

    Args:
        action: The index of the action that was taken.
        reward: The reward received for taking the action.
    """
    self.actionSelected[state, action] += 1
    self.stateVisit[state] += 1
    self.rewards[state, action] += reward
    
    
  def randomTieBreakArgmax(self, arr):
  
      max_value = max(arr)
      # Find indices of all elements equal to the maximum value
      max_indices = [i for i, x in enumerate(arr) if x == max_value]

      # If there's only one maximum, return its index directly
      if len(max_indices) == 1:
          return max_indices[0]

      # Randomly choose one index from the tie
      random_index = random.choice(max_indices)
      return random_index
        


# # Example usage
# env = # Your environment object (replace with your specific environment)
# ucb_agent = UCB(env.action_space.n)

# for episode in range(num_episodes):
#   state = env.reset()
#   done = False
#   while not done:
#     action = ucb_agent.choose_action(t)  # Choose action based on UCB
#     next_state, reward, done, info = env.step(action)  # Take action, observe outcome
#     ucb_agent.update(action, reward)  # Update agent's knowledge based on experience
#     state = next_state

# env.close()









# import numpy as np


# class UCB:
#   """
#   This class implements the UCB (Upper Confidence Bound) algorithm for reinforcement learning.
#   """

#   def __init__(self, numActions):
#     """
#     Initializes the UCB agent.

#     Args:
#         num_actions: The number of actions the agent can take.
#     """
#     self.numberOfActions = numActions
#     self.selections = np.zeros(numActions)  # Number of times each action has been selected
#     self.rewards = np.zeros(numActions)  # Sum of rewards for each action
#     self.c = np.sqrt(2) # Exploration parameter (controls the balance between exploitation and exploration)

#   def chooseAction(self, timeStep):
#     """
#     Chooses an action based on the UCB formula.

#     Args:
#         t: The current time step (used for calculating the confidence bound).

#     Returns:
#         The index of the chosen action.
#     """
#     if np.all(self.selections == 0):  # Initial exploration - choose random action if no selections yet
#       return np.random.choice(self.numberOfActions)

#     # Calculate average reward for each action (handling division by zero)
#     average_rewards = self.rewards / np.maximum(self.selections, 1)

#     # Calculate the UCB value for each action
#     ucbValues = average_rewards + self.c * np.sqrt(np.log(timeStep) / self.selections)

#     # Choose the action with the highest UCB value
#     return np.argmax(ucbValues)

#   def update(self, action, reward):
#     """
#     Updates the agent's knowledge based on the chosen action and received reward.

#     Args:
#         action: The index of the action that was taken.
#         reward: The reward received for taking the action.
#     """
#     self.selections[action] += 1
#     self.rewards[action] += reward


# # # Example usage
# # env = # Your environment object (replace with your specific environment)
# # ucb_agent = UCB(env.action_space.n)

# # for episode in range(num_episodes):
# #   state = env.reset()
# #   done = False
# #   while not done:
# #     action = ucb_agent.choose_action(t)  # Choose action based on UCB
# #     next_state, reward, done, info = env.step(action)  # Take action, observe outcome
# #     ucb_agent.update(action, reward)  # Update agent's knowledge based on experience
# #     state = next_state

# # env.close()