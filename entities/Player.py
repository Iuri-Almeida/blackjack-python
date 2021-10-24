class Player:
    """ Player representa a entidade do jogador que participa da partida de Blackjack.

    Attributes:
        name (str): Nome do jogador.
    """
    def __init__(self, name):
        """ (Player, str) -> Player

        Construtor: cria um objeto Player.
        """
        self.__name = name
        self.__points = 0
        self.__playing = True
        self.__overcomed = False
    
    def __str__(self):
        """ (Player) -> str

        Retorna uma string que o print() usa para imprimir um Player.
        """
        return f'name: {self.__name}, points: {self.__points}, playing: {self.__playing}, overcomed: {self.__overcomed}'

    def getName(self):
        """ (Player) -> str

        Recebe um Player e retorna o seu nome.
        """
        return self.__name
    
    def getPoints(self):
        """ (Player) -> int

        Recebe um Player e retorna a sua quantidade de pontos.
        """
        return self.__points
    
    def hasOvercomed(self):
        """ (Player) -> bool

        Recebe um Player e retorna se já ultrapassou 21 pontos.
        """
        return self.__overcomed
    
    def isPlaying(self):
        """ (Player) -> bool

        Recebe um Player e retorna se ainda está jogando.
        """
        return self.__playing

    def increasePoints(self, points):
        """ (Player, int) -> None

        Recebe um Player e um inteiro e modifica os pontos atuais somando com o inteiro de entrada.
        """
        self.__points += points
    
    def putSituation(self, playing):
        """ (Player, bool) -> None

        Recebe um Player e um bool e modifica a situação do Player em relação ao jogo (se ainda está jogando).
        """
        self.__playing = playing
    
    def putOvercomed(self, overcomed):
        """ (Player) -> None

        Recebe um Player e um bool e modifica as duas situações do Player (maior que 21 e se ainda está jogando).
        """
        self.__overcomed = overcomed
        self.putSituation(False)
