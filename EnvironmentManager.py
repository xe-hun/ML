# The EnvironmentManager ..

import numpy as np
import gymnasium as gym


class EnvironmentManager:
    def __init__(self, render=False):
        if render is True:
            self.env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False, render_mode = 'human')
        else:
            self.env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery=False)


        
        self.observation, info = self.env.reset()
        self.actionSpaceSize = self.env.action_space.n
        self.stateSpaceSize = self.env.observation_space.n
        
    def step(self, action):
        self.observation, reward, terminated, truncated, info = self.env.step(action)
        return reward, terminated or truncated
       
    
    def reset(self):
        self.env.reset()
       
        
    def close(self):
        self.env.close()
        
    # def render(self):
    #     pass
        
    # def num_actions_available(self):
    #     pass
        
    # def take_action(self, action):        
    #     pass
    
    # def get_state(self):
    #      pass
        
    # def num_state_features(self):
    #     pass