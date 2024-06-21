from Player import Player

class HumanPlayer(Player):

    def cardSelection(self):
        test = "wasKnown"
        line = int(input("Entrez la ligne de la carte\n"))-1
        column = int(input("Entrez la colonne de la carte\n"))-1
        if(self.knownHand[line][column] == "?"):
            test = "wasUnknown"
        self.knownHand[line][column] = self.realHand[line][column]
        return (self.knownHand[line][column], (line, column), test)
    
    def actionChoice(self):
        return int(input())
    
    def twoFirstCardsSelection(self):
        print(f"{self.name}, Choisissez deux cartes de votre choix dans votre jeu\n")
        lineFirst = int(input("Entrez la ligne de la première carte\n"))-1
        columnFirst = int(input("Entrez la colonne de la première carte\n"))-1
        self.knownHand[lineFirst][columnFirst] = self.realHand[lineFirst][columnFirst]
        lineSecond = int(input("Entrez la ligne de la deuxième carte\n"))-1
        columnSecond = int(input("Entrez la colonne de la deuxième carte\n"))-1
        while(lineFirst == lineSecond and columnFirst == columnSecond):
            print("Veuillez choisir une carte différente de la première\n")
            lineSecond = int(input("Entrez la ligne de la deuxième carte\n"))-1
            columnSecond = int(input("Entrez la colonne de la deuxième carte\n"))-1
        self.knownHand[lineSecond][columnSecond] = self.realHand[lineSecond][columnSecond]
        return (self.knownHand[lineFirst][columnFirst], self.knownHand[lineSecond][columnSecond])