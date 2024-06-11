import matplotlib.pyplot as plt
import numpy as np
is_ipython = 'inline' in plt.get_backend()
if is_ipython: from IPython import display

class Utility():
    def __init__(self):
        pass
        
    def plot(self, period, values):
        plt.figure(2)
        plt.clf()        
        plt.title('Training...')
        plt.xlabel('Episode')
        plt.ylabel('Duration')
        plt.plot(values)

        movingAverage = self.getMovingAverage2(period, values)
        plt.plot(movingAverage)    
        plt.pause(0.001)
        print("Episode", len(values), "\n", \
            period, "episode moving avg:", movingAverage[-1])
        # if is_ipython: display.clear_output(wait=True)

    def getMovingAverage(self, period:int, values:list):
        cumulativeSum = np.cumsum(values)
        movingAverage = np.zeros_like(values)
        
        for i in range(len(values)):
            if (i < period):
                movingAverage[i] = cumulativeSum[i] / (i + 1)
            else:
                movingAverage[i] = (cumulativeSum[i] - cumulativeSum[i - period]) / period
                
        return movingAverage
    
    def getMovingAverage2(self, period:int, vaules:list):
        N = len(vaules)
        movingAverage = np.empty(N)
        for t in range(N):
            movingAverage[t] = np.mean(vaules[max(0, t-period):(t+1)])

        return movingAverage
                
