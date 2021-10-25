"""
    Nome do Porjeto: Blackjack com POO
    Autor: Iuri Almeida
    Referências: https://github.com/Iuri-Almeida/blackjack
    Data: 24/10/2021
    Descrição: Jogo de Blackjack
    GitHub: https://github.com/Iuri-Almeida/blackjack-python
"""

from application.ui import UI
from application.constants import Constants
from entities.player import Player
from util.color import Color
from random import randint


def find_champion(players: list[Player]) -> list[Player]:
    """Encontra o campeão do jogo.

    Args:
        players: lista de jogadores

    Returns:
        list[Player]: lista de jogadores
    """
    champion = []

    for player in players:
        if not player.has_overcome:
            if not champion or (player.points == champion[0].points):
                champion.append(player)
            elif (Constants.TWENTY_ONE - player.points) < (Constants.TWENTY_ONE - champion[0].points):
                champion = [player]

    return champion


def get_card_value(card: str) -> int:
    """Pega o valor da carta.

    Args:
        card: caractere do baralho

    Returns:
        int: valor da carta
    """
    if card.isnumeric():
        return int(card)
    else:
        if card == 'A':
            return 1
        elif card == 'J':
            return 11
        elif card == 'Q':
            return 12
        elif card == 'K':
            return 13


def get_card(deck: list[str]) -> str:
    """Pega a carta no baralho de forma randômica.

    Args:
        deck: lista de caracteres

    Returns:
        str: carta do baralho
    """
    random_number = randint(0, len(deck) - 1)

    card = deck.pop(random_number)

    return card


def move(deck: list[str], player: Player) -> None:
    """Realiza a jogada na partida.

    Args:
        deck: lista de caracteres
        player: jogador

    Returns:
        None
    """
    answer = input(f"Você está com {Color.BOLD}{player.points}{Color.RESET} ponto(s). Deseja continuar? (s/n) ")
    answer = answer.strip().lower()
    while answer != 's' and answer != 'n':
        answer = input(f"{Color.COLOR_RED}Tente novamente. Deseja continuar? (s/n) {Color.RESET}").strip().lower()

    if answer == 's':

        card = get_card(deck)
        value = get_card_value(card)

        player.increase_points(value)

        print(f"Foi sorteado a carta {Color.BOLD}{card}{Color.RESET} cujo valor é {Color.BOLD}{value}{Color.RESET}. "
              f"Você agora está com {Color.BOLD}{player.points}{Color.RESET} ponto(s).")

    else:
        player.is_playing = False


def main() -> None:
    """Inicia o jogo.

    Returns:
        None
    """
    players: list[Player] = []

    UI.clear_screen()
    UI.show_title()

    n = input("Quantos jogadores jogarão? ")
    while not n.isnumeric() or int(n) > Constants.MAX_PLAYERS or int(n) < Constants.MIN_PLAYERS:
        n = input(f"{Color.COLOR_RED}Erro na entrada dos valores. Quantos jogadores jogarão? {Color.RESET}")

    UI.clear_screen()

    for i in range(int(n)):

        UI.show_player(i + 1)

        name = input("Digite o nome do jogador: ").strip().title()

        while not name:
            name = input("Digite um nome para o jogador: ").strip().title()

        player: Player = Player(name)

        players.append(player)

        UI.clear_screen()

    deck = Constants.CARDS

    while list(filter(lambda p: p.is_playing, players)) and deck:

        for player in players:

            if player.points <= Constants.TWENTY_ONE and player.is_playing:

                UI.show_player_turn(player.name)

                move(deck, player)

                if player.points > Constants.TWENTY_ONE:

                    player.has_overcome = True
                    print(f"\nJogador(a) {Color.BOLD}{player.name}{Color.RESET} já ultrapassou 21 pontos.")

                elif not player.is_playing:
                    print(f"\nJogador(a) {Color.BOLD}{player.name}{Color.RESET} decidiu parar de jogar.")

    champion = find_champion(players)

    if champion:
        UI.show_champion(champion)
    else:
        UI.no_champion()


if __name__ == "__main__":
    main()
