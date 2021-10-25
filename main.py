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
from random import randint
from typing import List


def find_champion(players: List[Player]) -> List[Player]:
    """Encontra o campeão do jogo.

    Keyword arguments:
        players -- lista de jogadores (type list[Player])
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

    Keyword arguments:
        card -- caractere do baralho (type str)
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


def get_card(deck: List[str]) -> str:
    """Pega a carta no baralho de forma randômica.

    Keyword arguments:
        deck -- lista de caracteres (type list[str])
    """
    random_number = randint(0, len(deck) - 1)

    card = deck.pop(random_number)

    return card


def move(deck: List[str], player: Player) -> None:
    """Realiza a jogada na partida.

    Keyword arguments:
        deck -- lista de caracteres (type list[str])
        player -- jogador (type Player)
    """
    answer = input(f"Você está com {player.points} ponto(s). Deseja continuar? (s/n) ").strip().lower()
    while answer != 's' and answer != 'n':
        answer = input(f"Tente novamente. Deseja continuar? (s/n) ").strip().lower()

    if answer == 's':

        card = get_card(deck)
        value = get_card_value(card)

        player.increase_points(value)

        print(f"Foi sorteado a carta {card} cujo valor é {value}. Você agora está com {player.points} ponto(s).")

    else:
        player.is_playing = False


def main() -> None:
    """Inicia o jogo.
    """
    players: list[Player] = []

    UI.clear_screen()
    UI.show_title()

    n = input("Quantos jogadores jogarão? ")
    while not n.isnumeric() or int(n) > Constants.MAX_PLAYERS or int(n) < Constants.MIN_PLAYERS:
        n = input("Erro na entrada dos valores. Quantos jogadores jogarão? ")

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
                    print(f"\nJogador(a) {player.name} já ultrapassou 21 pontos.")

                elif not player.is_playing:
                    print(f"\nJogador(a) {player.name} decidiu parar de jogar.")

    champion = find_champion(players)

    if champion:
        UI.show_champion(champion)
    else:
        UI.no_champion()


if __name__ == "__main__":
    main()
