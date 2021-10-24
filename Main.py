# Porjeto Blackjack com POO
# Autor: Iuri Almeida
# Referências: https://github.com/Iuri-Almeida/blackjack
# Data: 24/10/2021
# Descrição: Jogo de Blackjack

from application.UI import UI
from application.Constants import Constants
from entities.Player import Player
from random import randint


def getChampion(players):
    champion = []

    for player in players:
        if not player.hasOvercomed():
            if not champion or (player.getPoints() == champion[0].getPoints()): champion.append(player)
            elif (21 - player.getPoints()) < (21 - champion[0].getPoints()): champion = [player]
    
    return champion


def getCardValue(card):
    if card.isnumeric(): return int(card)
    else:
        if card == 'A': return 1
        elif card == 'J': return 11
        elif card == 'Q': return 12
        elif card == 'K': return 13


def getCardValues(deck):
    randomNumber = randint(0, len(deck) - 1)

    card = deck.pop(randomNumber)
    cardValue = getCardValue(card)

    return card, cardValue


def move(deck, player):
    answer = input(f"Você está com {player.getPoints()} ponto(s). Deseja continuar? (s/n) ").strip().lower()
    while answer != 's' and answer != 'n':
        answer = input(f"Tente novamente. Deseja continuar? (s/n) ").strip().lower()

    if answer == 's':

        card, value = getCardValues(deck)
        
        player.increasePoints(value)

        print(f"Foi sorteado a carta {card} cujo valor é {value}. Você agora está com {player.getPoints()} ponto(s).")
    
    else: player.putSituation(False)


def main():
    # Lista de jogadores
    players = []

    UI.clearScreen()
    UI.showTitle()

    n = input("Quantos jogadores jogarão? ")
    while not n.isnumeric() or int(n) > Constants.MAX_PLAYERS or int(n) < Constants.MIN_PLAYERS:
        n = input("Erro na entrada dos valores. Quantos jogadores jogarão? ")
    
    UI.clearScreen()

    for i in range(int(n)):

        UI.showPlayer(i)

        name = input("Digite o nome do jogador: ").strip().title()

        while not name:
            name = input("Digite um nome para o jogador: ").strip().title()

        player = Player(name)

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
