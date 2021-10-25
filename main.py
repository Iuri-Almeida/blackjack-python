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


def findChampion(players: List[Player]) -> List[Player]:
    """Encontra o campeão do jogo.

    Keyword arguments:
        players -- lista de jogadores (type list[Player])
    """
    champion = []

    for player in players:
        if not player.hasOvercomed:
            if not champion or (player.points == champion[0].points): champion.append(player)
            elif (21 - player.points) < (21 - champion[0].points): champion = [player]
    
    return champion


def getCardValue(card: str) -> int:
    """Pega o valor da carta.

    Keyword arguments:
        card -- caractere do baralho (type str)
    """
    if card.isnumeric(): return int(card)
    else:
        if card == 'A': return 1
        elif card == 'J': return 11
        elif card == 'Q': return 12
        elif card == 'K': return 13


def getCard(deck: List[str]) -> str:
    """Pega a carta no baralho de forma randômica.

    Keyword arguments:
        deck -- lista de caracteres (type list[str])
    """
    randomNumber = randint(0, len(deck) - 1)

    card = deck.pop(randomNumber)

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

        card = getCard(deck)
        value = getCardValue(card)
        
        player.increasePoints(value)

        print(f"Foi sorteado a carta {card} cujo valor é {value}. Você agora está com {player.points} ponto(s).")
    
    else: player.isPlaying = False


def main() -> None:
    """Inicia o jogo.
    """
    players: list[Player] = []

    UI.clearScreen()
    UI.showTitle()

    n = input("Quantos jogadores jogarão? ")
    while not n.isnumeric() or int(n) > Constants.MAX_PLAYERS or int(n) < Constants.MIN_PLAYERS:
        n = input("Erro na entrada dos valores. Quantos jogadores jogarão? ")
    
    UI.clearScreen()

    for i in range(int(n)):

        UI.showPlayer(i + 1)

        name = input("Digite o nome do jogador: ").strip().title()

        while not name:
            name = input("Digite um nome para o jogador: ").strip().title()

        player: Player = Player(name)

        players.append(player)

        UI.clearScreen()
    
    deck = Constants.CARDS

    while list(filter(lambda p: p.isPlaying, players)) and deck:

        for player in players:

            if player.points <= Constants.TWENTY_ONE and player.isPlaying:

                UI.showPlayerTurn(player.name)

                move(deck, player)

                if player.points > Constants.TWENTY_ONE:

                    player.hasOvercomed = True
                    print(f"\nJogador(a) {player.name} já ultrapassou 21 pontos.")
                
                elif not player.isPlaying: print(f"\nJogador(a) {player.name} decidiu parar de jogar.")
    
    champion = findChampion(players)

    if champion: UI.showChampion(champion)
    else: UI.noChampion()


if __name__ == "__main__":
    main()
