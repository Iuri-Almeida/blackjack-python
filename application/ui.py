from os import system
from typing import List
from entities.player import Player

class UI:
    """ UI representa a interface do usuário.
    """
    @staticmethod
    def clearScreen() -> None:
        """Limpa a tela do console.
        """
        system("clear")

    @staticmethod
    def showTitle() -> None:
        """Mostra o título do jogo.
        """
        print("### Seja bem vindo ao jogo Blackjack! ###\n")

    @staticmethod
    def showPlayer(i: int) -> None:
        """Mostra o número da vez do jogador.

        Keyword arguments:
            i -- valor (int)
        """
        print(f"\n----- Jogador {i} -----\n")

    @staticmethod
    def showPlayerTurn(name: str) -> None:
        """Mostra quando for a vez do jogador.

        Keyword arguments:
            name -- Nome do jogador (type str)
        """
        print(f"\n----- Vez de {name} -----\n")

    @staticmethod
    def showChampion(players: List[Player]) -> None:
        """Verifica se houve empate ou teve um campeão no jogo.

        Keyword arguments:
            players -- lista de jogadores (type list[Player])
        """
        if len(players) > 1:
            print("### Empate ###\n")
            for player in players:
                print(f"- {player.name} com {player.points} ponto(s).")
        else:
            print("\n### Ganhador(a) ###\n")
            print(f"{players[0].name} com {players[0].points} ponto(s).\n")

    @staticmethod
    def noChampion() -> None:
        """Mostra que todos os jogadores perderam.
        """
        print("\nTodos os jogadores perdaram.")