# The EnvironmentManager ..

import numpy as np
import gymnasium as gym
import abc


class EnvironmentManager(abc.ABC):
    
    def __init__(self, label:str, render:bool=False):
        if render is True:
            self.env = gym.make(label, render_mode = "human")
        else:
            self.env = gym.make(label)
        
        self.observation, info = self.env.reset()
        self.actionSpace = self.env.action_space
        self.ObservationSpace = self.env.observation_space
        
        
    def step(self, action):
        self.observation, reward, terminated, truncated, info = self.env.step(action)
        return reward, terminated or truncated
       
    
    def reset(self):
        self.observation, info = self.env.reset()
       
        
    def close(self):
        self.env.close()
        