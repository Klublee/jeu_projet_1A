# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 20:54:24 2020

@author: cbert
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:07:36 2020

@author: cbert
"""

## Jeu de course
## Règles :
    ## 2 joueurs
    ## 1 Dé
    ## On tire un dé à 6 faces à chaque tour
    ## Le premier arrivé à 10 gagne (amélioration possible en demandant le nombre de cases souhaitées)
    ## (Si au bout de 15 sec, le joueur n'a pas joué, l'ordinateur lance le dé automatiquement)
    
    
    
## Classes nécessaires :
    ## Plateau
    ## Pion
    ## Case


##Choix du nom des joueurs
##joueur1=input("Nom du joueur 1 :")
##joueur2=input("Nom du joueur 2 :")
## Choix de la taille du plateau
##nombre_cases=input("Combien de cases voulez-vous ?")
nombre_cases=10

import tkinter as tk
import random
from PIL import Image, ImageTk
import time
## Liste des noms d'image pour le dé
dé = ['Dé 1.png', 'Dé 2.png', 'Dé 3.png', 'Dé 4.png', 'Dé 5.png', 'Dé 6.png']

## Création de la classe dé
class Dé:
    def __init(self):
        self.fen_princ = tk.Tk()
        self.fen_princ.geometry('800x700')
        self.fen_princ.title('Lancer le Dé')
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dé)))
        label= tk.Label(self.fen_princ, text='', font=('Arial', 500))
        self.label1 = tk.Label(self.fen_princ, image=image1)
        self.label1.image = image1
        self.label1.pack()
        bouton=tk.Button(self.fen_princ, text='lancer le Dé', foreground='black', command=self.lancer)
        bouton.pack()
        self.fen_princ.mainloop()

    def lancer():
        nombre=random.randint(0,5)
        image1 = ImageTk.PhotoImage(Image.open(dé[nombre]))
        self.label1.configure(image=image1)
        self.label1.image = image1
        print("Résultat : ",nombre+1)
        return(nombre+1)
   
    def fermer(self):
       self.root.destroy()


## Création de la classe pion
class Pion:
    def __init__(self,couleur,position,):
        self.couleur = couleur
        self.position = position
        ##self.image=##nom de l'image
        
    def changer_position(self,pos):
        self.position=pos
        


## Création de la classe case
class case :
    def __init__(self,numéro,activité):
        self.numéro=numéro
        self.activité=activité

        

##Création des 2 pions
Pion_1=Pion('b',0)
Pion_2=Pion('r',0)



print("Le joueur 1 est case :",Pion_1.position)
print("Le joueur 2 est case :",Pion_2.position)


##Création des cases
Case_0=case(0,False)
librairie_cases={} ## librairie dans laquelle on crée le reste des cases
for i in range (nombre_cases+1):
    if i==0:
        librairie_cases['Case_'+str(i)]=case(i,False)
    else:
        librairie_cases['Case_'+str(i)]=case(i,True)
    

## Lancement du jeu

jeu=True
while jeu==True:
    print ("Tour du joueur 1")
    nombre=Dé.lancer()
    time.sleep(1000)
    Pion_1.changer_position(Pion_1.position+nombre)
    print("Position du joueur 1 :",Pion_1.position)
    Dé.fermer()
    if Pion_1.position>=nombre_cases :
        print("Victoire du joueur 1")
        break
    print("Tour du joueur 2")
    nombre=Dé.lancer()
    time.sleep(1000)
    Pion_2.changer_position(Pion_2.position+nombre)
    print("Position du joueur 2 :",Pion_2.position)
    Dé.fermer()
    if Pion_2.position>=nombre_cases :
        print("Victoire du joueur 2")
        break
    


