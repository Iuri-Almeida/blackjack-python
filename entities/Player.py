class Player:
    """ Player representa a entidade do jogador que participa da partida de Blackjack.

    Attributes:
        name (str): Nome do jogador.
    """
    def __init__(self, name: str) -> None:
        """ (Player, str) -> Player

        Construtor: cria um objeto Player.
        """
        self.__name = name
        self.__points: int = 0
        self.__isPlaying: bool = True
        self.__hasOvercomed: bool = False

    def __str__(self) -> str:
        """ (Player) -> str

        Retorna uma string que o print() usa para imprimir um Player.
        """
        return f'name: {self.__name}, points: {self.__points}, isPlaying: {self.__isPlaying}, hasOvercomed: {self.__hasOvercomed}'

    @property
    def name(self) -> str:
        """ (Player) -> str

        Recebe um Player e retorna o seu nome.
        """
        return self.__name

    @property
    def points(self) -> int:
        """ (Player) -> int

        Recebe um Player e retorna a sua quantidade de pontos.
        """
        return self.__points

    @property
    def hasOvercomed(self) -> bool:
        """ (Player) -> bool

        Recebe um Player e retorna se já ultrapassou 21 pontos.
        """
        return self.__hasOvercomed

    @hasOvercomed.setter
    def hasOvercomed(self, hasOvercomed: bool) -> None:
        """ (Player) -> None

        Recebe um Player e um bool e modifica as duas situações do Player (maior que 21 e se ainda está jogando).
        """
        if isinstance(hasOvercomed, bool):
            self.__hasOvercomed = hasOvercomed
            self.isPlaying = False
        else: raise TypeError(f'Parâmetro {hasOvercomed} precisa ser do tipo bool.')

    @property
    def isPlaying(self) -> bool:
        """ (Player) -> bool

        Recebe um Player e retorna se ainda está jogando.
        """
        return self.__isPlaying

    @isPlaying.setter
    def isPlaying(self, isPlaying: bool) -> None:
        """ (Player, bool) -> None

        Recebe um Player e um bool e modifica a situação do Player em relação ao jogo (se ainda está jogando).
        """
        if isinstance(isPlaying, bool): self.__isPlaying = isPlaying
        else: raise TypeError(f'Parâmetro {isPlaying} precisa ser do tipo bool.')

    def increasePoints(self, points: int) -> None:
        """ (Player, int) -> None

        Recebe um Player e um inteiro e modifica os pontos atuais somando com o inteiro de entrada.
        """
        if isinstance(points, int): self.__points += points
        else: raise TypeError(f'Parâmetro {points} precisa ser do tipo int.')
