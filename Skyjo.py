import numpy as np
from Player import Player  # Importer correctement la classe Player

class Skyjo:
    # Se déroule en plusieurs manches et se termine dès qu'un joueur atteint 100 points ou plus. Celui qui a obtenu le moins de points gagne la partie.
    def __init__(self, playersList):
        self.draw = np.random.permutation(list(np.fromiter([-2] * 5 + [0] * 15 + [nombre for nombre in range(-1, 13) for _ in range(10)], dtype=int)))
        self.playersList = []  # Utiliser une liste pour les joueurs (plus flexible)
        self.discard = []
        for name in playersList:
            hand = []
            for _ in range(3):  # Distribuer 3 ensembles de 4 cartes par joueur
                hand.append(self.draw[:4].tolist())  # Distribuer efficacement 4 cartes et retirer du paquet
                self.draw = self.draw[4:]
            newPlayer = Player(hand, name)
            self.playersList.append(newPlayer)  # Ajouter les objets Joueur à la liste
        self.seenCards = np.array([])
        self.playerTurn = self.playersList[0]

    def displayHands(self):
        for player in self.playersList:
            print(player)
            
    def displayPlayerHand(self, player):
        print(player)
        
    def reorderPlayers(players, startingPlayer):
        return players[players.index(startingPlayer):] + players[:players.index(startingPlayer)]
    
    def unpileDraw(self):
        unpiledCard = self.draw[0]
        self.seenCards.append(unpiledCard)
        self.discard.append(unpiledCard)
        return 
            
    def jouerPartie(self):
        print("Bienvenue dans le Skyjo !\nDistribution des cartes :\n")
        self.displayHands()
        biggestPlayerDelta = ("x", -10) # Choix du premier à jouer
        for player in self.playersList:
            couple = player.twoFirstCardsSelection()
            self.seenCards.append(couple[0])
            self.seenCards.append(couple[1])
            self.displayPlayerHand(player)
            if(abs(couple[0]-couple[1]) > biggestPlayerDelta[1]):
                biggestPlayerDelta = (player, abs(couple[0]-couple[1]))
        print("Voici les cartes choisies par tout le monde :\n")
        self.displayHands()
        self.playerTurn = biggestPlayerDelta[0]
        print(f"{self.playerTurn.name} a la plus grande différence de cartes et commence à jouer !\n")
        self.playersList = self.reorderPlayers(self.playersList, self.playerTurn)
        print(f"Ordre des joueurs : {self.playersList}")
        while all(player.score < 100 for player in self.playersList):
            self.playRound()

    def playRound(self): #faire commencer à jouer le bon joueur stocké dans self.playerTurn
        currentPlayer = self.playerTurn
        for player in self.playersList:
            for notYou in self.playersList:
                if(notYou.name != player.name):
                    print(f"Jeu de {notYou.name} : \n {notYou}")
            print(f"Carte de la pile : {self.draw[0]}\nVotre jeu : \n {player}\nVotre score : {player.score}\nVoulez vous prendre la carte de la pile (entrez '1') ou une carte de la pioche (entrez '2') ?\nVotre choix : ")
            player.play(self)#donner toutes les données du jeu
                

    def afficher_scores(self):
        for player in self.playersList:
            print(f"Score de {player.name} : {player.score}")

# Définir les joueurs et initialiser le jeu
players = ["Alice", "Bob"]
game = Skyjo(players)
game.jouerPartie()