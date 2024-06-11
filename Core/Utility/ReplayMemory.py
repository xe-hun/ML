import random

class ReplayMemory():
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.memory = []
        self.push_count = 0
        
    def push(self, experience):
        if len(self.memory) < self.capacity:
            self.memory.append(experience)
        else:
            self.memory[self.push_count % self.capacity] = experience
        self.push_count += 1
        
    def sample(self, batchSize):
        return random.sample(self.memory, batchSize)
    
    def canProvideSample(self, batchSize):
        return len(self.memory) >= batchSize
    
    
    