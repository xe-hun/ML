from Core.Policy import Policy as Base
from Core.Utility.Helper import Helper
import numpy as np
import random

class DoubleQLearningPolicy(Base):
    def  __init__(self):
       self.learningRate = .001
    
    def initializePolicy(self, stateSpace, actionSpaceSize:int):
        self.Q = {}
        self.Q2 = {}
        self.actionSpaceSize = actionSpaceSize
        
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(actionSpaceSize)]
                
        for s in stateSpace:
                self.Q2[s] = [initialQValue for _ in range(actionSpaceSize)]
                
        return self.Q, self.Q2
    
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
    
    def train(self, currentState:int, nextState:int, reward:int, action:int, selectionPolicy:Base):
        # if(currentState == nextState):
        #     return
        
        alpha = self.learningRate #learningRate
        gamma = .9 #discountFactor
        # gamma = .999 #discountFactor
        selectionPolicyMaxAction =  selectionPolicy.getMaxAction(currentState)
        self.Q[currentState][action] = self.Q[currentState][action] + alpha * (reward + gamma * self.Q[nextState][selectionPolicyMaxAction] - self.Q[currentState][action])
        
  