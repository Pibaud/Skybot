import numpy as np
from Player import Player

class Skyjo:
    # Se déroule en plusieurs manches et se termine dès qu'un joueur atteint 100 points ou plus. Celui qui a obtenu le moins de points gagne la partie.
    def __init__(self, playersList):
        self.draw = np.array([])
        self.namesList = playersList
        self.playersList = []
        self.discard = []
        self.seenCards = []
        self.playerTurn = None

    def displayHands(self):
        for player in self.playersList:
            print(player)
            
    def displayPlayerHand(self, player):
        print(player)
        
    def reorderPlayers(self):
        return self.playersList[self.playersList.index(self.playerTurn):] + self.playersList[:self.playersList.index(self.playerTurn)]
    
    def unpileDraw(self):
        unpiledCard = self.draw[0]
        self.seenCards.append(unpiledCard)
        self.discard.append(unpiledCard)
        return 
    
    def displayAllRealHands(self):
        for player in self.playersList:
            player.revealAll()
        self.displayHands()
            
    def jouerPartie(self):
        print("Bienvenue dans le Skyjo !\nDistribution des cartes...\n")
        self.displayHands()
        while all(player.score < 100 for player in self.playersList):
            biggestPlayerSum = ("x", -10) # Choix du premier à jouer
            for player in self.playersList:
                couple = player.twoFirstCardsSelection()
                self.seenCards.append(couple[0])
                self.seenCards.append(couple[1])
                self.displayPlayerHand(player)
                if(couple[0]+couple[1] > biggestPlayerSum[1]):
                    biggestPlayerSum = (player, couple[0]+couple[1])
            print("Voici les cartes choisies par tout le monde :\n")
            self.displayHands()
            self.playerTurn = biggestPlayerSum[0]
            print(f"{self.playerTurn.name} a la plus grande somme de cartes et commence à jouer !\n")
            self.playersList = self.reorderPlayers()
            print(f"Ordre des joueurs : {self.playersList}")
            self.playRound()
            self.displayScores()
            for player in self.playersList:
                player.resetHasFinished()

    def playRound(self):
        self.draw = np.random.permutation(list(np.fromiter([-2] * 5 + [0] * 15 + [nombre for nombre in range(-1, 13) for _ in range(10)], dtype=int)))
        self.discard = [self.draw[0]]
        for name in self.namesList:
            hand = []
            for _ in range(3):  # Distribuer 3 ensembles de 4 cartes par joueur
                hand.append(self.draw[:4].tolist())  # Distribuer efficacement 4 cartes et retirer du paquet
                self.draw = self.draw[4:]
            newPlayer = Player(hand, name)
            self.playersList.append(newPlayer)  # Ajouter les objets Joueur à la liste
        self.seenCards = [self.discard[0]]
        self.playerTurn = self.playersList[0]
        while(True):
            for player in self.playersList:
                for notYou in self.playersList:
                    if(notYou.name != player.name):
                        print(f"Jeu de {notYou.name} :\n {notYou}")
                print(f"Carte de la pile : {self.discard[-1]}\nVotre jeu : \n {player}\nVotre score : {player.score}\nVoulez vous prendre la carte de la pile (entrez '1') ou une carte de la pioche (entrez '2') ?\nVotre choix : ")
                newGameState = player.play(self.draw, self.discard, self.seenCards)
                self.draw = newGameState[0]
                self.discard = newGameState[1]
                self.seenCards = newGameState[2]
                if(player.hasFinished):
                    self.playerTurn = player
                    remainingPlayers = self.reorderPlayers()
                    remainingPlayers = remainingPlayers[1:] # on obtient la liste des joueurs qui doivent finir de jouer
                    for remainingPlayer in remainingPlayers :
                        for notYou in remainingPlayers:
                            if(notYou.name != remainingPlayer.name):
                                print(f"Jeu de {notYou.name} :\n {notYou}")
                        print(f"Carte de la pile : {self.discard[-1]}\nVotre jeu : \n {remainingPlayer}\nVotre score : {remainingPlayer.score}\nVoulez vous prendre la carte de la pile (entrez '1') ou une carte de la pioche (entrez '2') ?\nVotre choix : ")
                        newGameState = remainingPlayer.play(self.draw, self.discard, self.seenCards)
                        self.draw = newGameState[0]
                        self.discard = newGameState[1]
                        self.seenCards = newGameState[2]
                    print(f"C'est fini ! Tout le monde retourne ses cartes !")
                    self.displayAllRealHands()
                    return 0

    def displayScores(self):
        for player in self.playersList:
            print(f"Score de {player.name} : {player.score}")

players = ["Alice", "Bob"]
game = Skyjo(players)
game.jouerPartie()