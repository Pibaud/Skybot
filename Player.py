class Player:
    def __init__(self, hand, name):
        self.realHand = hand  # La main réelle est maintenant une liste de listes
        self.knownHand = [['?' for _ in range(4)] for _ in range(3)]  # Initialiser la main connue avec des "?"
        self.name = name
        self.score = 0

    def __str__(self):
        res = f"{self.name}:\n"
        for ligne in self.knownHand:  # Pour chaque sous-liste de la main connue
            chaine_ligne = ""
            for element in ligne:
                chaine_ligne += f"{element:>5}"  # Formater les éléments avec 5 espaces
            res += chaine_ligne + "\n"
        return res
    
    def cardSelection(self):
        line = int(input("Entrez la ligne de la carte\n"))-1
        column = int(input("Entrez la colonne de la carte\n"))-1
        self.knownHand[line][column] = self.realHand[line][column]
        return (self.knownHand[line][column], (line, column))

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
    
    def play(self, draw, discard, seenCards):
        choice = int(input()) # Mettre l'IA ici
        while(choice != 1 or choice != 2):
                choice = int(input("Erreur, veuillez choisir 1 ou 2 :\n"))
        if(choice == 1):
            print(f"Vous prenez la carte {discard[len(discard)-1]} de la pile\nAvec quelle carte de votre main voulez-vous l'échanger ?\n")
            print(self)
            cardAndCoord = self.cardSelection()
            print(f"Vous échangez un {cardAndCoord[0]} contre un {discard[len(discard)-1]}")
            self.knownHand[cardAndCoord[1][0]][cardAndCoord[1][1]] = discard[len(discard)-1]
            seenCards.append(cardAndCoord[0])
            discard.append