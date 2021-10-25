# Porjeto Blackjack com POO
# Autor: Iuri Almeida
# Referências: https://github.com/Iuri-Almeida/blackjack
# Data: 24/10/2021
# Descrição: Jogo de Blackjack

from application.UI import UI
from application.Constants import Constants
from entities.Player import Player
from random import randint
from typing import List


def getChampion(players: List[Player]) -> List[Player]:
    """ (list<Player>) -> list<Player>

    Recebe uma lista de Player e retorna uma nova lista de player, podendo estar vazia.
    """
    champion = []

    for player in players:
        if not player.hasOvercomed():
            if not champion or (player.getPoints() == champion[0].getPoints()): champion.append(player)
            elif (21 - player.getPoints()) < (21 - champion[0].getPoints()): champion = [player]
    
    return champion


def getCardValue(card: str) -> int:
    """ (str) -> int

    Recebe um str e retorna um int baseado no seu valor no baralho.
    """
    if card.isnumeric(): return int(card)
    else:
        if card == 'A': return 1
        elif card == 'J': return 11
        elif card == 'Q': return 12
        elif card == 'K': return 13


def getCard(deck: List[str]) -> str:
    """ (list<str>) -> str

    Recebe uma lista de str e retorna um str do baralho.
    """
    randomNumber = randint(0, len(deck) - 1)

    card = deck.pop(randomNumber)

    return card


def move(deck: List[str], player: Player) -> None:
    """ (list<str>, Player) -> None

    Recebe uma lista de str e um Player e modifica seus valores conforme forem jogando.
    """
    answer = input(f"Você está com {player.getPoints()} ponto(s). Deseja continuar? (s/n) ").strip().lower()
    while answer != 's' and answer != 'n':
        answer = input(f"Tente novamente. Deseja continuar? (s/n) ").strip().lower()

    if answer == 's':

        card = getCard(deck)
        value = getCardValue(card)
        
        player.increasePoints(value)

        print(f"Foi sorteado a carta {card} cujo valor é {value}. Você agora está com {player.getPoints()} ponto(s).")
    
    else: player.putSituation(False)


def main() -> None:
    """ (None) -> None

    Função principal do jogo Blackjack.
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

    while list(filter(lambda p: p.isPlaying(), players)) and deck:

        for player in players:

            if player.getPoints() <= Constants.TWENTY_ONE and player.isPlaying():

                UI.showPlayerTurn(player.getName())

                move(deck, player)

                if player.getPoints() > Constants.TWENTY_ONE:

                    player.putOvercomed(True)
                    print(f"\nJogador(a) {player.getName()} já ultrapassou 21 pontos.")
                
                elif not player.isPlaying(): print(f"\nJogador(a) {player.getName()} decidiu parar de jogar.")
    
    champion = getChampion(players)

    if champion: UI.showChampion(champion)
    else: UI.noChampion()


if __name__ == "__main__":
    main()
