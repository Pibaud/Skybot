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

    def twoFirstCardsSelection(self):
        print("Choisissez deux cartes de votre choix dans votre jeu\n")
        lineFirst = int(input("Entrez la ligne de la première carte"))-1
        columnFirst = int(input("Entrez la colonne de la première carte"))-1
        self.knownHand[lineFirst][columnFirst] = self.realHand[lineFirst][columnFirst]
        lineSecond = int(input("Entrez la ligne de la deuxième carte"))-1
        columnSecond = int(input("Entrez la colonne de la deuxième carte"))-1
        while(lineFirst == lineSecond and columnFirst == columnSecond):
            print("Veuillez choisir une carte différente de la première")
            lineSecond = int(input("Entrez la ligne de la deuxième carte"))-1
            columnSecond = int(input("Entrez la colonne de la deuxième carte"))-1
        self.knownHand[lineSecond][columnSecond] = self.realHand[lineSecond][columnSecond]
        return ((self.knownHand[lineFirst][columnFirst], self.knownHand[lineSecond][columnSecond]), self.knownHand)
        