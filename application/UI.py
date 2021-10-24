from os import system

class UI:

    @staticmethod
    def clearScreen():
        system("clear")

    @staticmethod
    def showTitle():
        print("### Seja bem vindo ao jogo Blackjack! ###\n")

    @staticmethod
    def showPlayer(i):
        print(f"\n----- Jogador {i + 1} -----\n")

    @staticmethod
    def showPlayerTurn(name):
        print(f"\n----- Vez de {name} -----\n")

    @staticmethod
    def showChampion(players):
        if len(players) > 1:
            print("### Empate ###\n")
            for player in players:
                print(f"- {player.getName()} com {player.getPoints()} ponto(s).")
        else:
            print("\n### Ganhador(a) ###\n")
            print(f"{players[0].getName()} com {players[0].getPoints()} ponto(s).\n")

    @staticmethod
    def noChampion():
        print("\nTodos os jogadores perdaram.")
