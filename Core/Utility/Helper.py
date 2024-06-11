import random
import matplotlib.pyplot as plt
import numpy as np
is_ipython = 'inline' in plt.get_backend()
if is_ipython: from IPython import display

class Helper():
    def __init__(self):
        pass
    
    @staticmethod
    def getMovingAverage3(period:int, values:list):
        t = len(values)
        return np.mean(values[max(0, t-period):(t + 1)])
    
    @staticmethod
    def randomTieBreakArgmax(arr):
    
        max_value = max(arr)
        # Find indices of all elements equal to the maximum value
        max_indices = [i for i, x in enumerate(arr) if x == max_value]

        # If there's only one maximum, return its index directly
        if len(max_indices) == 1:
            return max_indices[0]

        # Randomly choose one index from the tie
        random_index = random.choice(max_indices)
        return random_index
    
    @staticmethod   
    def sum_lists(list1, list2):
        """
        This function takes two lists and returns a new list containing the sum of corresponding elements.

        Args:
            list1: The first list.
            list2: The second list.

        Returns:
            A new list containing the sum of corresponding elements from list1 and list2.

        Raises:
            ValueError: If the lists have different lengths.
        """

        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length for element-wise sum.")

        list3 = [x + y for x, y in zip(list1, list2)]
        return list3


            
                
            
        
    
    # @staticmethod
    # def plot(self, period, values):
    #     plt.figure(2)
    #     plt.clf()        
    #     plt.title('Training...')
    #     plt.xlabel('Episode')
    #     plt.ylabel('Duration')
    #     plt.plot(values)

    #     movingAverage = self.getMovingAverage2(period, values)
    #     plt.plot(movingAverage)    
    #     plt.pause(0.001)
    #     print("Episode", len(values), "\n", \
    #         period, "episode moving avg:", movingAverage[-1])
        # if is_ipython: display.clear_output(wait=True)

    # @staticmethod
    # def getMovingAverage(self, period:int, values:list):
    #     cumulativeSum = np.cumsum(values)
    #     movingAverage = np.zeros_like(values)
        
    #     for i in range(len(values)):
    #         if (i < period):
    #             movingAverage[i] = cumulativeSum[i] / (i + 1)
    #         else:
    #             movingAverage[i] = (cumulativeSum[i] - cumulativeSum[i - period]) / period
                
    #     return movingAverage
    
    # @staticmethod    
    # def getMovingAverage2(self, period:int, vaules:list):
    #     N = len(vaules)
    #     movingAverage = np.empty(N)
    #     for t in range(N):
    #         movingAverage[t] = np.mean(vaules[max(0, t-period):(t+1)])

    #     return movingAverage
    
   
                
