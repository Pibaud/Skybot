from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, hand, name):
        self.realHand = hand  # La main réelle est maintenant une liste de listes
        self.knownHand = [['?' for _ in range(4)] for _ in range(3)]  # Initialiser la main connue avec des "?"
        self.name = name
        self.totalScore = 0
        self.roundScore = 0
        self.hasFinished = False

    def __str__(self):
        res = f"{self.name}:\n"
        for row in self.knownHand:  # Pour chaque sous-liste de la main connue
            string = ""
            for element in row:
                string += f"{element:>5}"  # Formater les éléments avec 5 espaces
            res += string + "\n"
        return res
    
    def setHasFinished(self):
        self.hasFinished = True
        
    def resetHasFinished(self):
        self.hasFinished = False
        
    def resetRoundScore(self):
        self.roundScore = 0
        
    def revealAll(self):
        self.knownHand = self.realHand
        self.calculateScore()
        self.totalScore += self.roundScore
    
    @abstractmethod
    def cardSelection(self):
        pass
    
    def revealCheck(self):
        return all(cell != "?" for row in self.knownHand for cell in row)
    
    def columnTest(self, discard):
        for col in range(0, len(self.knownHand[0])-1):
            first_card = self.knownHand[0][col]
            all_same = True
            for row in range(1, 3):
                if(self.knownHand[row][col] != first_card):
                    all_same = False
                    break
            if (all_same and first_card != "?"):
                
                for row in range(3):
                    discard.append(self.knownHand[row][col])
                    del self.knownHand[row][col]
                    del self.realHand[row][col]
                print(f"Vous avez une colonne complète de {first_card} ! Elle est enlevée de votre jeu")
        return discard
    
    def calculateScore(self):
        total = 0
        for row in self.knownHand:
            for element in row:
                if(element != "?"):
                    total += element
        self.roundScore = total
    
    @abstractmethod
    def actionChoice(self):
        pass

    @abstractmethod
    def twoFirstCardsSelection(self):
        pass
    
    def play(self, draw, discard, seenCards):
        print(f"Je sais que les cartes qui ont été jouées sont :\n{seenCards}\n\nVoulez vous prendre la carte de la pile (entrez '1') ou une carte de la pioche (entrez '2') ?\nVotre choix : \n")
        firstChoice = self.actionChoice() # Mettre l'IA ici
        while(firstChoice != 1 and firstChoice != 2):
                firstChoice = int(input("Erreur, veuillez choisir 1 ou 2 :\n"))
        if(firstChoice == 1):
            print(f"Vous prenez la carte {discard[-1]} de la pile\nAvec quelle carte de votre main voulez-vous l'échanger ?\n")
            cardAndCoord = self.cardSelection()
            print(f"Vous échangez un {cardAndCoord[0]} contre un {discard[len(discard)-1]}")
            self.knownHand[cardAndCoord[1][0]][cardAndCoord[1][1]] = discard[len(discard)-1]
            self.realHand[cardAndCoord[1][0]][cardAndCoord[1][1]] = discard[len(discard)-1]
            discard = discard[:len(discard)-2]
            discard.append(cardAndCoord[0])
            if(cardAndCoord[2] == "wasUnknown"):
                seenCards.append(cardAndCoord[0])
        else:
            print(f"Vous piochez\nLa carte obtenue est un {draw[0]}\nVoulez-vous l'échanger avec une de vos cartes (entrez '1') ou la poser sur la défausse et retourner une de vos cartes cachées (entrez '2') ?\n")
            seenCards.append(draw[0])
            secondChoice = self.actionChoice()
            while(secondChoice != 1 and secondChoice != 2):
                secondChoice = int(input("Erreur, veuillez choisir 1 ou 2 :\n"))
            if(secondChoice == 1):
                cardAndCoord = self.cardSelection()
                print(f"Vous échangez un {cardAndCoord[0]} contre un {draw[0]}")
                self.knownHand[cardAndCoord[1][0]][cardAndCoord[1][1]] = draw[0]
                self.realHand[cardAndCoord[1][0]][cardAndCoord[1][1]] = draw[0]
                discard.append(cardAndCoord[0])
                if(cardAndCoord[2] == "wasUnknown"):
                    seenCards.append(cardAndCoord[0])
            else:
                print(f"Vous posez la carte {draw[0]} sur la défausse")
                discard.append(draw[0])
                draw = draw[1:]
                flippedCard = self.cardSelection()
                while(flippedCard[2] != "wasUnknown"):
                    print(f"La carte doit être inconnue\n")
                    flippedCard = self.cardSelection()
                print(f"Vous retournez une carte, c'est un {flippedCard[0]}")
        discard = self.columnTest(discard)
        if(self.revealCheck()):
            print(f"{self.name} a retourné sa dernière carte ! C'est le dernier tour pour les autres joueurs !")
            self.setHasFinished()
        self.calculateScore()
        return(draw, discard, seenCards)