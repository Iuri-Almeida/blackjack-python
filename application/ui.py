from os import system
from entities.player import Player
from util.color import Color


class UI(object):
    """UI representa a interface do usuário.
    """
    @staticmethod
    def clear_screen() -> None:
        """Limpa a tela do console.

        Returns:
            None
        """
        system("clear")

    @staticmethod
    def show_title() -> None:
        """Mostra o título do jogo.

        Returns:
            None
        """
        print(f"{Color.BOLD}{Color.COLOR_YELLOW}### {Color.REVERSE}Seja bem vindo ao jogo Blackjack!{Color.RESET}"
              f"{Color.BOLD}{Color.COLOR_YELLOW} ###{Color.RESET}\n")

    @staticmethod
    def show_player(i: int) -> None:
        """Mostra o número da vez do jogador.

        Args:
            i: valor

        Returns:
            None
        """
        print(f"\n{Color.BOLD}{Color.COLOR_LIGHT_BLUE}----- {Color.REVERSE}Jogador {i}{Color.RESET}{Color.BOLD}"
              f"{Color.COLOR_LIGHT_BLUE} -----{Color.RESET}\n")

    @staticmethod
    def show_player_turn(name: str) -> None:
        """Mostra quando for a vez do jogador.
        
        Args:
            name: Nome do jogador
        
        Returns:
            None
        """
        print(f"\n{Color.BOLD}{Color.COLOR_PURPLE}----- {Color.REVERSE}Vez de {name}{Color.RESET}{Color.BOLD}"
              f"{Color.COLOR_PURPLE} -----{Color.RESET}\n")

    @staticmethod
    def show_champion(players: list[Player]) -> None:
        """Verifica se houve empate ou teve um campeão no jogo.

        Args:
            players: lista de jogadores

        Returns:
            None
        """
        if len(players) > 1:
            print(f"{Color.BOLD}{Color.COLOR_GREEN}### {Color.REVERSE}Empate{Color.RESET}{Color.BOLD}"
                  f"{Color.COLOR_GREEN} ###{Color.RESET}\n")
            for player in players:
                print(f"- {Color.BOLD}{player.name}{Color.RESET} com {Color.BOLD}{player.points}"
                      f"{Color.RESET} ponto(s).")
        else:
            print(f"\n{Color.BOLD}{Color.COLOR_GREEN}### {Color.REVERSE}Ganhador(a){Color.RESET}{Color.BOLD}"
                  f"{Color.COLOR_GREEN} ###{Color.RESET}\n")
            print(f"{Color.BOLD}{players[0].name}{Color.RESET} com {Color.BOLD}{players[0].points}"
                  f"{Color.RESET} ponto(s).\n")

    @staticmethod
    def no_champion() -> None:
        """Mostra que todos os jogadores perderam.

        Returns:
            None
        """
        print(f"\n{Color.BOLD}Todos os jogadores perdaram.{Color.RESET}")
