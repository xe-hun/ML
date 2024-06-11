from Core.Policy import Policy as Base
from Core.Utility.Helper import Helper
import numpy as np
import random

class Policy(Base):
    def  __init__(self):
       self.learningRate = .001
    
    def initializePolicy(self, stateSpace, actionSpaceSize:int):
        self.Q = {}
        self.actionSpaceSize = actionSpaceSize
        
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(actionSpaceSize)]
        return self.Q
    
    def getMaxAction(self, state)->int:
        return Helper.randomTieBreakArgmax(self.Q[state])
    
    def getRandomAction(self)->int:
        return random.randrange(self.actionSpaceSize);
        
    def setTrainingRate(self, learningRate:float)->int:
        self.learningRate = learningRate
        
    def getActionWithExploration(self, explorationRate:float, state:tuple):
        if(explorationRate > random.random()):
            return self.getRandomAction()
        else:
            return self.getMaxAction(state)
    
    def train(self, currentState:int, nextState:int, reward:int, action:int):
        # if(currentState == nextState):
        #     return
        
        alpha = self.learningRate #learningRate
        gamma = .9 #discountFactor
        # gamma = .999 #discountFactor
        self.Q[currentState][action] = self.Q[currentState][action] + alpha * (reward + gamma * max(self.Q[nextState]) - self.Q[currentState][action])
      
        

    
        
        
       