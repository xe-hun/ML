from typing import Optional
import numpy as np

class Agent():
    # def __init__(self, strategy, num_actions, device):
    def __init__(self):
        # self.current_step = 0
        # self.strategy = strategy
        # self.num_actions = num_actions
        # self.device = device
        
        self.cartPositionSpace = np.linspace(-2.4, 2.4, 20)
        self.cartVelocitySpace = np.linspace(-4, 4, 20)
        self.poleAngleSpace = np.linspace(-0.20943951, 0.20943951, 20)
        self.poleAngleVelocitySpace = np.linspace(-4, 4, 20)
        
        # self.cartPositionSpace = np.linspace(-2.4, 2.4, 8)
        # self.cartVelocitySpace = np.linspace(-4, 4, 5)
        # self.poleAngleSpace = np.linspace(-0.20943951, 0.20943951, 3)
        # self.poleAngleVelocitySpace = np.linspace(-4, 4, 3)
        # self.stateSpace = []
        
        
    def initializeState(self):
        stateSpace = []
        
        for i in range(len(self.cartPositionSpace)):
            for j in range(len(self.cartVelocitySpace)):
                for k in range(len(self.poleAngleSpace)):
                    for l in range(len(self.poleAngleVelocitySpace)):
                        stateSpace.append((i, j, k, l))
                        
        return stateSpace

    def getState(self, observation:tuple)->tuple:
        cartPosition, cartVelocity, poleAngle, poleAngleVelocity = observation
        cartPosition = np.digitize(cartPosition, self.cartPositionSpace[:-1], True)
        cartVelocity = np.digitize(cartVelocity, self.cartVelocitySpace[:-1], True)
        poleAngle = np.digitize(poleAngle, self.poleAngleSpace[:-1], True)
        poleAngleVelocity = np.digitize(poleAngleVelocity, self.poleAngleVelocitySpace[:-1], True)
        
        return (cartPosition, cartVelocity, poleAngle, poleAngleVelocity)
        

    # def selectAction(self, state:tuple, policy, explorationRate:Optional[float] = None)->int:
    #     if(explorationRate is None):
    #         return policy.getMaxAction(state)
    #     else:
    #         return policy.getActionWithStrategy(explorationRate, state)
   