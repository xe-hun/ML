import numpy as np
import random
class Policy:
    def  __init__(self):
       pass
    
    def initializeQValues(self, stateSpace, actionSpaceSize:int):
        self.Q = {}
        self.actionSpaceSize = actionSpaceSize
        
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(actionSpaceSize)]
        return self.Q
    
    def getMaxAction(self, state)->int:
        return np.argmax(self.Q[state])
    
    def getRandomAction(self)->int:
        return random.randrange(self.actionSpaceSize);
        # return random.choice(list(range(self.numberOfAction)));
    
    def getActionWithStrategy(self, explorationRate:float, state:tuple):
        if(explorationRate > random.random()):
            return self.getRandomAction()
        else:
            return self.getMaxAction(state)
    
    def train(self, currentState:tuple, nextState:tuple, reward:int, action:int):
        if(currentState == nextState):
            return
        
        alpha = .01 #learningRate
        gamma = .9 #discountFactor
        qsetter = self.Q[currentState][action] + alpha * (reward + gamma * max(self.Q[nextState]) - self.Q[currentState][action])
        self.Q[currentState][action] = qsetter
        
    
    # def updateQValue(self):
    #     pass
    
    
    # # def train(sel):
    
    # def getQValue(self, state):
    #     # if(self.Q == None) 
    #     # then you must initialize q value first
    #     return self.Q[state]
        