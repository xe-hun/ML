# The EnvironmentManager ..

import numpy as np
import gymnasium as gym


class EnvironmentManager:
    def __init__(self):
        env = gym.make('CartPole-v1')
        env.reset()
        
   
    
   
       
    
    def reset(self):
        pass
       
        
    def close(self):
        pass
        
    def render(self):
        pass
        
    def num_actions_available(self):
        pass
        
    def take_action(self, action):        
        pass
    
    def get_state(self):
         pass
        
    def num_state_features(self):
        pass