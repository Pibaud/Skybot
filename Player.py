class Player:
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name
        self.score = 0
    def __str__(self):
        res = ""
        for ligne in self.hand:
            chaine_ligne = ""
            for element in ligne:
                chaine_ligne += f"{element:>5}"  # Formatage des éléments avec 5 espaces
            res += chaine_ligne + "\n"
        return res