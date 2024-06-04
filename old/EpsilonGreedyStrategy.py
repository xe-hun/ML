import math

class EpsilonGreedyStrategy():
    def __init__(self, start, end, decay):
        self.start = start
        self.end = end
        self.decay = decay
    
    def getExplorationRate(self, currentStep:int)->float:
        return self.end + (self.start - self.end) * \
            math.exp(-1. * currentStep * self.decay)
            
    def chooseAction(self, state, policy, timeStep)->int:
        explorationRate = self.getExplorationRate(timeStep)
        return policy.getActionWithExploration(explorationRate, state)