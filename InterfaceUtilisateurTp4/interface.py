import tkinter as tk
from tkinter import ttk
import datetime
import serial
from moduleTp4 import Captation
import json




s = serial.Serial("COM6")

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Captation des mesures")
        self.geometry("700x700")
        
        self.dateHeureMesure  = ""
        self.dataMesure = []

      
        self.bouton_demarrer_captation = tk.Button(text="Démarrer sytème de captation",  font=("Times New Roman", 10), takefocus=True)
        self.bouton_demarrer_captation["command"] = self.bouton_demarrer_syteme
        self.bouton_demarrer_captation.place(x=220, y=0)
        
        self.label_description = tk.Label(text="Description mesure:", font=("Times New Roman", 10))
        self.label_description.place(x=50, y=50)
        
        self.text_box_descripton = tk.Entry(width=20)
        self.text_box_descripton['state'] = "disabled"
        self.text_box_descripton.place(x=50, y=85)
        
        
        self.liste_journal_mesure = tk.Listbox(width=75, height=30)
        self.liste_journal_mesure.place(x=235, y=100)
        
        self.bouton_detecter_mouvement = tk.Button(text="Détecter mouvement",  font=("Times New Roman", 10))   
        self.bouton_detecter_mouvement["command"] = self.bouton_mesure
        self.bouton_detecter_mouvement['state'] = "disabled"
        self.bouton_detecter_mouvement.place(x=50, y=120)

        
        
        self.label_actif = tk.Label(text="DÉSACTIVÉ", font=("Times New Roman", 10), bg="red")
        self.label_actif.place(x=50, y=155)
        
        
    def bouton_demarrer_syteme(self):
        s.write(b"ON\n")
        self.label_actif['text'] = "ACTIVÉ"
        self.label_actif['bg'] = "green"
        self.bouton_detecter_mouvement['state'] = 'normal'
        self.text_box_descripton['state'] = 'normal'
        
 
        
        
    def bouton_mesure(self):
        self.dateHeureMesure = datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p")
        if self.text_box_descripton.get() == "":
            s.write(b"Description vide\n")
            self.bouton_detecter_mouvement['state'] = 'disabled'
            self.text_box_descripton['state'] = 'disabled'
            self.label_actif['text'] = "DÉSACTIVÉ"
            self.label_actif['bg'] = "red"
            self.description = "Aucune description saisie"
            self.captation = Captation(str(self.dateHeureMesure),self.description, self.dataMesure)
            self.liste_journal_mesure.insert("end",self.captation.__repr__())

        else:
            
            s.write(b"Description valide\n")
            self.bouton_detecter_mouvement['state'] = 'disabled'
            self.text_box_descripton['state'] = 'disabled'
            
            
            self.label_actif['text'] = "DÉSACTIVÉ"
            self.label_actif['bg'] = "red"

            
            self.captation = Captation(str(self.dateHeureMesure),  str(self.text_box_descripton.get()), self.dataMesure )
            
            self.liste_journal_mesure.insert("end",self.captation.__repr__())
             
            
    
        
if __name__ == '__main__':
    app = Interface()
    app.mainloop()