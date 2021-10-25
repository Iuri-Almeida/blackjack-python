class Player:
    """ Player representa a entidade do jogador que participa da partida de Blackjack.

    Attributes:
        name -- Nome do jogador (type str)
        points -- Pontos do jogador (type int)
        isPlaying -- Se esse jogador está jogando (type bool)
        hasOvercomed -- Se esse jogador ultrapassou 21 pontos (type bool)
    """
    def __init__(self, name: str) -> None:
        """Construtor: cria um objeto Player.

        Keyword arguments:
            name -- Nome do jogador (type str)
        """
        self.__name = name
        self.__points: int = 0
        self.__isPlaying: bool = True
        self.__hasOvercomed: bool = False

    def __str__(self) -> str:
        """Monta o texto para ser apresentado na tela.
        """
        return f'name: {self.__name}, points: {self.__points}, isPlaying: {self.__isPlaying}, hasOvercomed: {self.__hasOvercomed}'

    @property
    def name(self) -> str:
        """Propriedade get do nome.
        """
        return self.__name

    @property
    def points(self) -> int:
        """Propriedade get dos pontos.
        """
        return self.__points

    @property
    def hasOvercomed(self) -> bool:
        """Propriedade get para saber se o jogador ultrapassou os 21 pontos.
        """
        return self.__hasOvercomed

    @hasOvercomed.setter
    def hasOvercomed(self, hasOvercomed: bool) -> None:
        """Propriedade set para definir se o jogador ultrapassou os 21 pontos.

        Keyword arguments:
            hasOvercomed -- booleano (type bool)
        """
        if isinstance(hasOvercomed, bool):
            self.__hasOvercomed = hasOvercomed
            self.isPlaying = False
        else: raise TypeError(f'Parâmetro {hasOvercomed} precisa ser do tipo bool.')

    @property
    def isPlaying(self) -> bool:
        """Propriedade get para saber se o jogador ainda está jogando.
        """
        return self.__isPlaying

    @isPlaying.setter
    def isPlaying(self, isPlaying: bool) -> None:
        """Propriedade set para definir se o jogador vai continuar jogando.

        Keyword arguments:
            isPlaying -- booleano (type bool)
        """
        if isinstance(isPlaying, bool): self.__isPlaying = isPlaying
        else: raise TypeError(f'Parâmetro {isPlaying} precisa ser do tipo bool.')

    def increasePoints(self, points: int) -> None:
        """Faz o incremento dos pontos do jogador.

        Keyword arguments:
            points -- pontos a serem acrescidos (type int)
        """
        if isinstance(points, int): self.__points += points
        else: raise TypeError(f'Parâmetro {points} precisa ser do tipo int.')