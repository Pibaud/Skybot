import numpy as np
import Player

class Skyjo:
    # Se déroule en plusieurs manches et se termine dès qu'un joueur atteint 100 points ou plus. Celui qui a obtenu le moins de points gagne la partie.
    def __init__(self, playersList):
        self.draw = np.random.permutation(list(np.fromiter([-2] * 5 + [0] * 15 + [nombre for nombre in range(-1, 13) for _ in range(10)], dtype=int))) # les 150 cartes
        self.playedCards = np.array([])
        hands = np.array([[[self.draw[j:j + 4], '?'] for j in range(i * 4, (i + 1) * 4)] for i in range(playersList.shape[0])])
        self.draw = self.draw[hands.size:]  # Remove dealt cards from deck
        self.playersList = np.array([Player(hand.tolist(), player) for hand, player in zip(hands, playersList)])
        
players = ["Alice", "Bob", "Charlie", "David"]
game = Skyjo(np.array(players))
for player in game.playersList:
    print("jeu de",player.name,":",player.hand,"\n")
print("pioche :",game.draw)
rfffff