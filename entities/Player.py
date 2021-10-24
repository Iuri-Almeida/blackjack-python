class Player:
    def __init__(self, name):
        self.__name = name
        self.__points = 0
        self.__playing = True
        self.__overcomed = False
    
    def __str__(self):
        return f'name: {self.__name}, points: {self.__points}, playing: {self.__playing}, overcomed: {self.__overcomed}'

    def getName(self):
        return self.__name
    
    def getPoints(self):
        return self.__points
    
    def hasOvercomed(self):
        return self.__overcomed
    
    def isPlaying(self):
        return self.__playing

    def increasePoints(self, points):
        self.__points += points
    
    def putSituation(self, playing):
        self.__playing = playing
    
    def putOvercomed(self, overcomed):
        self.__overcomed = overcomed
        self.putSituation(False)
