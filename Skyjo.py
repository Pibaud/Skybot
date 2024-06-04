import numpy as np
from Player import Player  # Importer correctement la classe Player

class Skyjo:
    # Se déroule en plusieurs manches et se termine dès qu'un joueur atteint 100 points ou plus. Celui qui a obtenu le moins de points gagne la partie.
    def __init__(self, playersList):
        self.draw = np.random.permutation(list(np.fromiter([-2] * 5 + [0] * 15 + [nombre for nombre in range(-1, 13) for _ in range(10)], dtype=int)))
        self.playersList = []  # Utiliser une liste pour les joueurs (plus flexible)
        for name in playersList:
            hand = []
            for _ in range(3):  # Distribuer 3 ensembles de 4 cartes par joueur
                hand.append(self.draw[:4].tolist())  # Distribuer efficacement 4 cartes et retirer du paquet
                self.draw = self.draw[4:]
            newPlayer = Player(hand, name)
            self.playersList.append(newPlayer)  # Ajouter les objets Joueur à la liste
        self.playedCards = np.array([])
        self.playerTurn = self.playersList[0]

    def afficher_mains(self):
        for player in self.playersList:
            print(player)

    def jouerPartie(self):
        biggestPlayerDelta = ("x", -10) # Choix du premier à jouer
        for player in self.playersList:
            couple = player.twoFirstCardsSelection()
            # révéler les cartes choisies
            if(abs(couple[0]-couple[1]) > biggestPlayerDelta[1]):
                biggestPlayerDelta = (player.name, abs(couple[0]-couple[1]))
        self.playerTurn = biggestPlayerDelta[0]
        print(f"{self.playerTurn.name} commence à jouer !\n")
        while all(player.score < 100 for player in self.playersList):
            self.jouerManche()
            self.afficher_scores()

    def jouerManche(self):
        for player in self.playersList:
            for notYou in self.playersList:
                if(notYou.name != player.name):
                    print(f"Jeu de {notYou.name} : \n {notYou}")
            print(f"Votre jeu : \n {player}")
            print(f"Carte de la pile : {self.draw[0]}")
            print(f"Score de {player.name} : {player.score}")

    def afficher_scores(self):
        for player in self.playersList:
            print(f"Score de {player.name} : {player.score}")

# Définir les joueurs et initialiser le jeu
players = ["Alice", "Bob", "Charlie", "David"]
game = Skyjo(players)
game.jouerPartie()