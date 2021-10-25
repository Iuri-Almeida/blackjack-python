class Player:
    """ Player representa a entidade do jogador que participa da partida de Blackjack.

    Attributes:
        name -- Nome do jogador (type str)
        points -- Pontos do jogador (type int)
        is_playing -- Se esse jogador está jogando (type bool)
        has_overcome -- Se esse jogador ultrapassou 21 pontos (type bool)
    """
    def __init__(self, name: str) -> None:
        """Construtor: cria um objeto Player.

        Keyword arguments:
            name -- Nome do jogador (type str)
        """
        self.__name = name
        self.__points: int = 0
        self.__is_playing: bool = True
        self.__has_overcome: bool = False

    @property
    def __str__(self) -> str:
        """Monta o texto para ser apresentado na tela.

        Returns:
            object:
        """
        return f'name: {self.__name}, points: {self.__points}, is_playing: {self.__is_playing}, ' \
               f'has_overcome: {self.__has_overcome} '

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
    def has_overcome(self) -> bool:
        """Propriedade get para saber se o jogador ultrapassou os 21 pontos.
        """
        return self.__has_overcome

    @has_overcome.setter
    def has_overcome(self, has_overcome: bool) -> None:
        """Propriedade set para definir se o jogador ultrapassou os 21 pontos.

        Keyword arguments:
            has_overcome -- booleano (type bool)
        """
        if isinstance(has_overcome, bool):
            self.__has_overcome = has_overcome
            self.is_playing = False
        else:
            raise TypeError(f'Parâmetro {has_overcome} precisa ser do tipo bool.')

    @property
    def is_playing(self) -> bool:
        """Propriedade get para saber se o jogador ainda está jogando.
        """
        return self.__is_playing

    @is_playing.setter
    def is_playing(self, is_playing: bool) -> None:
        """Propriedade set para definir se o jogador vai continuar jogando.

        Keyword arguments:
            is_playing -- booleano (type bool)
        """
        if isinstance(is_playing, bool):
            self.__is_playing = is_playing
        else:
            raise TypeError(f'Parâmetro {is_playing} precisa ser do tipo bool.')

    def increase_points(self, points: int) -> None:
        """Faz o incremento dos pontos do jogador.

        Keyword arguments:
            points -- pontos a serem acrescidos (type int)
        """
        if isinstance(points, int):
            self.__points += points
        else:
            raise TypeError(f'Parâmetro {points} precisa ser do tipo int.')
