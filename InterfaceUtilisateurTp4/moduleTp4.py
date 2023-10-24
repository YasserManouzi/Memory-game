
class Captation:
    
    def __init__(self, dateHeureMesure, descritpion, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.description = descritpion
        self.dataMesure = dataMesure
        
    def __repr__(self):
        return self.dateHeureMesure + " , " + self.description
    
    def afficherMesure(self):
        return self.dateHeureMesure  + ", " + "\n" + self.description + ", " +"\n" + self.dataMesure