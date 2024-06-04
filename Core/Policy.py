import abc

class Policy(abc.ABC):
    
    @abc.abstractmethod
    def initializePolicy(self, stateSpace, actionSpaceSize:int):
       pass
    
    @abc.abstractmethod
    def getMaxAction(self, state)->int:
        pass
        
    @abc.abstractmethod
    def getRandomAction(self)->int:
        pass
        
    @abc.abstractmethod
    def setTrainingRate(self, learningRate:float)->int:
        pass
        
    @abc.abstractmethod
    def getActionWithExploration(self, explorationRate:float, state:tuple):
       pass
    
    @abc.abstractmethod
    def train(self, currentState:int, nextState:int, reward:int, action:int):
        pass
      
       