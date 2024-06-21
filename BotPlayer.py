from Player import Player
import random

class BotPlayer(Player):
    def cardSelection(self):
        # IA basique pour le choix de la carte
        unknown_cards = [(r, c) for r in range(len(self.knownHand)) for c in range(len(self.knownHand[r])) if self.knownHand[r][c] == '?']
        if unknown_cards:
            line, column = random.choice(unknown_cards)
            self.knownHand[line][column] = self.realHand[line][column]
            return (self.knownHand[line][column], (line, column), "wasUnknown")
        else:
            line = random.randint(0, len(self.knownHand) - 1)
            column = random.randint(0, len(self.knownHand[0]) - 1)
            return (self.knownHand[line][column], (line, column), "wasKnown")

    def actionChoice(self):
        # IA basique pour le choix de l'action
        return random.choice([1, 2])

    def twoFirstCardsSelection(self):
        # IA basique pour la sélection des deux premières cartes
        choices = []
        for _ in range(2):
            line = random.randint(0, len(self.knownHand) - 1)
            column = random.randint(0, len(self.knownHand[0]) - 1)
            while (line, column) in choices:
                line = random.randint(0, len(self.knownHand) - 1)
                column = random.randint(0, len(self.knownHand[0]) - 1)
            self.knownHand[line][column] = self.realHand[line][column]
            choices.append