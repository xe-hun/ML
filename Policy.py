import numpy as np
import random
class Policy:
    def  __init__(self):
       self.learningRate = .005
    
    def initializeQValues(self, stateSpace, actionSpaceSize:int):
        self.Q = {}
        self.actionSpaceSize = actionSpaceSize
        
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(actionSpaceSize)]
        return self.Q
    
    def getMaxAction(self, state)->int:
        return self.randomTieBreakArgmax(self.Q[state])
    
    def getRandomAction(self)->int:
        return random.randrange(self.actionSpaceSize);
        # return random.choice(list(range(self.numberOfAction)));
        
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
        gamma = .999 #discountFactor
        self.Q[currentState][action] = self.Q[currentState][action] + alpha * (reward + gamma * max(self.Q[nextState]) - self.Q[currentState][action])
      
        

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
        
        
            # def randomTieBreakArgmax(self, arr):
 
    #     # Find the maximum value(s)
    #     max_value = arr.max()
    #     # Find indices of all elements equal to the maximum value
    #     max_indices = np.flatnonzero(arr == max_value)

    #     # If there's only one maximum, return its index directly
    #     if len(max_indices) == 1:
    #         return max_indices[0]

    #     # Randomly choose one index from the tie
    #     random_index = np.random.choice(max_indices)
    #     return random_index
