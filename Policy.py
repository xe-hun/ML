import numpy as np
import random
class Policy:
    def  __init__(self, strategy):
       pass
    
    def initializeQValues(self, stateSpace, numberOfAction:int):
        self.Q = {}
        self.numberOfAction = numberOfAction
        
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(numberOfAction)]
        return self.Q
    
    def getAction(self, state)->int:
        return np.argmax(self.Q[state])
    
    def getRandomAction(self)->int:
        return random.randrange(self.numberOfAction);
        # return random.choice(list(range(self.numberOfAction)));
    
    def getActionWithStrategy(self, explorationRate:float, state:tuple):
        if(explorationRate > random.random()):
            return self.getRandomAction()
        else:
            return self.getAction(state)
    
    def train(self, currentState:tuple, nextState:tuple, reward:int):
        alpha = .001
        gamma = .08
        self.Q[currentState] = alpha * (reward + gamma * self.Q[nextState]) 
        pass
    
    # def updateQValue(self):
    #     pass
    
    
    # # def train(sel):
    
    # def getQValue(self, state):
    #     # if(self.Q == None) 
    #     # then you must initialize q value first
    #     return self.Q[state]
        