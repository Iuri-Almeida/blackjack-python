class Player(object):
    """Player representa a entidade do jogador que participa da partida de Blackjack.

    Attributes:
        name -- Nome do jogador (type str)
        points -- Pontos do jogador (type int)
        is_playing -- Se esse jogador está jogando (type bool)
        has_overcome -- Se esse jogador ultrapassou 21 pontos (type bool)
    """
    def __init__(self, name: str) -> None:
        """Construtor: cria um objeto Player.

        Args:
            name: Nome do jogador
        """
        self.__name = name
        self.__points: int = 0
        self.__is_playing: bool = True
        self.__has_overcome: bool = False

    @property
    def __str__(self) -> str:
        """Monta o texto para ser apresentado na tela.

        Returns:
            str: texto com os atributos da classe Player
        """
        return f'name: {self.__name}, points: {self.__points}, is_playing: {self.__is_playing}, ' \
               f'has_overcome: {self.__has_overcome} '

    @property
    def name(self) -> str:
        """Propriedade get do nome.

        Returns:
            str: nome do jogador
        """
        return self.__name

    @property
    def points(self) -> int:
        """Propriedade get dos pontos.

        Returns:
            int: quantidade de pontos
        """
        return self.__points

    @property
    def has_overcome(self) -> bool:
        """Propriedade get para saber se o jogador ultrapassou os 21 pontos.

        Returns:
            bool: se o jogador ultrapassou 21 pontos
        """
        return self.__has_overcome

    @has_overcome.setter
    def has_overcome(self, has_overcome: bool) -> None:
        """Propriedade set para definir se o jogador ultrapassou os 21 pontos.

        Args:
            has_overcome: booleano

        Returns:
            None
        """
        if isinstance(has_overcome, bool):
            self.__has_overcome = has_overcome
            self.is_playing = False
        else:
            raise TypeError(f'Parâmetro {has_overcome} precisa ser do tipo bool.')

    @property
    def is_playing(self) -> bool:
        """Propriedade get para saber se o jogador ainda está jogando.

        Returns:
            bool: se o jogador ainda está jogando
        """
        return self.__is_playing

    @is_playing.setter
    def is_playing(self, is_playing: bool) -> None:
        """Propriedade set para definir se o jogador vai continuar jogando.

        Args:
            is_playing: booleano

        Returns:
            None
        """
        if isinstance(is_playing, bool):
            self.__is_playing = is_playing
        else:
            raise TypeError(f'Parâmetro {is_playing} precisa ser do tipo bool.')

    def increase_points(self, points: int) -> None:
        """Faz o incremento dos pontos do jogador.

        Args:
            points: pontos a serem acrescidos

        Returns:
            None
        """
        if isinstance(points, int):
            self.__points += points
        else:
            raise TypeError(f'Parâmetro {points} precisa ser do tipo int.')
