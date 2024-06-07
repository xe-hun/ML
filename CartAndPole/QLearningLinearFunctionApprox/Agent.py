from Core.Agent import Agent as Base
import numpy as np
  
class Agent(Base):
    def __init__(self):
        self.cartPositionMin, self.cartPositionMax = -2.4, 2.4
        self.cartVelocityMin, self.cartVelocityMax = -3.0, 3.0
        self.poleAngleMin, self.poleAngleMax = -0.20943951, 0.20943951
        self.poleAngularVelocityMin, self.poleAngularVelocityMax = -4.0, 4.0

        self.numPositionBin = 8
        self.numVelocityBin = 8
        self.numAngleBin = 8
        self.numAngularVelocityBin = 8
        
        self.cartPositionBin = np.linspace(self.cartPositionMin, self.cartPositionMax, self.numPositionBin + 1)
        self.cartVelocityBin = np.linspace(self.cartVelocityMin, self.cartVelocityMax, self.numVelocityBin + 1)
        self.poleAngleBin = np.linspace(self.poleAngleMin, self.poleAngleMax, self.numAngleBin + 1)
        self.poleAngularVelocityBin = np.linspace(self.poleAngularVelocityMin, self.poleAngularVelocityMax, self.numAngularVelocityBin + 1)
        
       
       
        
    def initializeState(self):
        stateSpace = []
        
        for i in range(len(self.cartPositionSpace)):
            for j in range(len(self.cartVelocitySpace)):
                for k in range(len(self.poleAngleSpace)):
                    for l in range(len(self.poleAngleVelocitySpace)):
                        stateSpace.append((i, j, k, l))
                        
        return stateSpace

    def getState(self, observation:tuple)->tuple:
        cartPosition, cartVelocity, poleAngle, poleAngularVelocity = observation
        numWeights = self.numTilings * (self.numVelocityBin + self.numPositionBin + self.numAngleBin + self.numAngularVelocityBin)

        featureVector = np.zeros(numWeights)
        activeTiles = self.tiles(cartPosition, cartVelocity, poleAngle, poleAngularVelocity)
        for tile_index in activeTiles:
            featureVector[tile_index] = 1
            
        return featureVector
        
    def tiles(self, cartPosition, cartVelocity, poleAngle, poleAngularVelocity):
        tileIndices = []
        numTilings = 3
        
        for tiling in range(numTilings):
            cartPositionOverLappingUnit = tiling * (self.cartPositionMax - self.cartPositionMin) / (self.numPositionBin * numTilings)
            cartVelocityOverLappingUnit = tiling * (self.cartVelocityMax - self.cartVelocityMin) / (self.numVelocityBin * numTilings)
            poleAngleOverLappingUnit = tiling * (self.poleAngleMax - self.poleAngleMin) / (self.numAngleBin * numTilings)
            poleAngularVelocityOverLappingUnit = tiling * (self.poleAngularVelocityMax - self.poleAngularVelocityMin) / (self.numAngularVelocityBin * numTilings)
            
            cartPositionIndex = np.digitize(cartPosition, self.cartPositionBin + cartPositionOverLappingUnit)
            cartVelocityIndex = np.digitize(cartVelocity, self.cartVelocityBin + cartVelocityOverLappingUnit)
            poleAngleIndex = np.digitize(poleAngle, self.poleAngleBin + poleAngleOverLappingUnit)
            poleAngularVelocityIndex = np.digitize(poleAngularVelocity, self.poleAngularVelocityBin + poleAngularVelocityOverLappingUnit)
            
            tileIndex = (tiling * (self.numPositionBin + self.numVelocityBin + self.numAngleBin + self.numAngularVelocityBin)
                        + cartPositionIndex 
                        + cartVelocityIndex * self.numPositionBin
                        + poleAngleIndex * self.numPositionBin * self.numVelocityBin
                        + poleAngularVelocityIndex * self.numAngleBin * self.numPositionBin * self.numVelocityBin
                        )
            
            tileIndices.append(tileIndex)
            
            return tileIndices
    
