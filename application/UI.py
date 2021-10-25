from os import system
from typing import List
from entities.Player import Player

class UI:
    """ UI representa a interface do usuário.
    """
    @staticmethod
    def clearScreen() -> None:
        """ (None) -> None

        Não recebe nada e executa o comando para limpar a tela do console.
        """
        system("clear")

    @staticmethod
    def showTitle() -> None:
        """ (None) -> None

        Não recebe nada e executa o comando para mostrar na tela o título.
        """
        print("### Seja bem vindo ao jogo Blackjack! ###\n")

    @staticmethod
    def showPlayer(i: int) -> None:
        """ (int) -> None

        Recebe um inteiro e executa o comando para mostrar na tela o número da vez.
        """
        print(f"\n----- Jogador {i} -----\n")

    @staticmethod
    def showPlayerTurn(name: str) -> None:
        """ (str) -> None

        Recebe uma str e executa o comando para mostrar na tela o nome do Player da vez.
        """
        print(f"\n----- Vez de {name} -----\n")

    @staticmethod
    def showChampion(players: List[Player]) -> None:
        """ (list<Player>) -> None

        Recebe uma list de Player e executa o comando para mostrar na tela o se houve um único ganhador ou empate.
        """
        if len(players) > 1:
            print("### Empate ###\n")
            for player in players:
                print(f"- {player.getName()} com {player.getPoints()} ponto(s).")
        else:
            print("\n### Ganhador(a) ###\n")
            print(f"{players[0].getName()} com {players[0].getPoints()} ponto(s).\n")

    @staticmethod
    def noChampion() -> None:
        """ (None) -> None

        Não recebe nada e executa o comando para mostrar na tela que todos os Players perderam.
        """
        print("\nTodos os jogadores perdaram.")
