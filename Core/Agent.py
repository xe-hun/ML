
import abc

class Agent(abc.ABC):

    @abc.abstractmethod  
    def initializeState(self):
        pass

    @abc.abstractmethod  
    def getState(self, observation):
        pass