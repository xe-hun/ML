
class Policy:
    def  __init__(self):
        pass
    
    def initializeQValues(self, stateSpace, numberOfAction):
        self.Q = {}
        initialQValue = 0
        for s in stateSpace:
                self.Q[s] = [initialQValue for _ in range(numberOfAction)]
        return self.Q
    
    def updateQValue(self):
        pass
    
    # def train(sel):
    
    def getQValue(self, state):
        # if(self.Q == None) 
        # then you must initialize q value first
        return self.Q[state]
        