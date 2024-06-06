import numpy as np
from Player import Player

class Skyjo:
    # Se déroule en plusieurs manches et se termine dès qu'un joueur atteint 100 points ou plus. Celui qui a obtenu le moins de points gagne la partie.
    def __init__(self, playersList):
        self.namesList = playersList
        self.playersList = []
        self.isGameFinished = False

    def displayHands(self):
        for player in self.playersList:
            print(player)
            
    def setGameIsFinished(self):
        self.isGameFinished = True
            
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
        
    def displayOrder(self):
        string = ""
        for player in self.playersList:
            string += player.name+" "
        print(f"L'ordre est le suivant : {string}\n")
            
    def jouerPartie(self):
        print("Bienvenue dans le Skyjo !")
        while (not self.isGameFinished):
            self.playRound()
            self.displayScores()
            for player in self.playersList:
                player.resetHasFinished()
                if(player.score >= 100):
                    self.setGameIsFinished()

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
        self.displayHands()
        biggestPlayerSum = ("x", -10) # Choix du premier à jouer
        for player in self.playersList:
            couple = player.twoFirstCardsSelection()
            self.seenCards.append(couple[0])
            self.seenCards.append(couple[1])
            self.displayPlayerHand(player)
            if(couple[0]+couple[1] > biggestPlayerSum[1]):
                biggestPlayerSum = (player, couple[0]+couple[1])
        self.playerTurn = biggestPlayerSum[0]
        print(f"{self.playerTurn.name} a la plus grande somme de cartes et commence à jouer !\n")
        self.playersList = self.reorderPlayers()
        self.displayOrder()
        while(True):
            for player in self.playersList:
                for notYou in self.playersList:
                    if(notYou.name != player.name):
                        print(f"{notYou}")
                print(f"VOUS :\n {player}\nCarte de la pile : {self.discard[-1]}\nSCORE : {player.score}\n")
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
                        print(f"VOUS : \n {remainingPlayer}\nCarte de la pile : {self.discard[-1]}\nVotre score : {remainingPlayer.score}")
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

players = []
nbPlayers = int(input("Entrez le nombre de joueurs :\n"))
for i in range(nbPlayers):
    players.append(input(f"Entrez le nom du joueur {i+1} :\n"))
game = Skyjo(players)
game.jouerPartie()