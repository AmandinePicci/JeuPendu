#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 13:16:44 2020
@author: amandine

Le jeu du pendu version graphique.

TODO :
Pour cette version, vous aurez besoin : 
    •d’un bouton (pour proposer) 
    •de deux label  (pour afficher le mot en cours de recherche et pour afficher le nombre coups restants
    
1) Le cœur du programme se déclenche lorsqu’on clique sur le bouton PROPOSER. 
2) On pourra ensuite modifier le comportement de ce bouton pour commencer une nouvelle partie 
3) Pourquoi pas ajouter un affichage des meilleurs scores en fin de partie. 
    
FAIT :
    •d’un Entry (pour saisir des lettres) 
    •d’un canvas sur lequel déposer une image du pendu 

"""

#IMPORTATION BIBLIOTHEQUES
import fcts_pendu as f
from tkinter import Tk, Label, Button, StringVar, Entry
from tkinter import Canvas, PhotoImage



#PP
fenetre = Tk()                                                                      #Création fenêtre graphique
fenetre.title ('Le jeu du Pendu')
fenetre.geometry ('1000x800+100+40')
#-------------------------------------------------------------------------------------------------------------------------------
Label1 = Label(fenetre, text = 'Saisie de lettre :')                                #Permet de saisir une lettre
Label1.pack(side='left', padx=5)
saisielettre = StringVar()
Champ = Entry (fenetre, textvariable=saisielettre, bg='cyan4', fg='white')
Champ.focus_set()
Champ.pack(side='left', padx=5)
#-------------------------------------------------------------------------------------------------------------------------------
def Mot ():
    global texte
    mot=f.CacheMot(f.ChoixMot())
    texte.set("Le mot à deviner est \n"+ mot)

texte=StringVar()                                                               #Permet de montrer le mot à deviner
Mot()
LabelMot=Label(fenetre, textvariable= texte , fg='white', bg='red')
LabelMot.pack(side='top',padx=40, pady=5)
#-------------------------------------------------------------------------------------------------------------------------------

buttonPropose = Button(fenetre, text="PROPOSER", bg='cyan4', fg='white')             #Permet de lancer la proposition de la lettre
buttonPropose.pack(side='left', padx=5, pady=4)                                     #Bouton ne sert à rien pour l'instant il faut mettre une command avec
                                                                                    #une fonction du pendu 
#-------------------------------------------------------------------------------------------------------------------------------
im='bonhomme1.gif'
can1 = Canvas(fenetre, width =400, height =400, bg ='white')                        #Permet d'afficher une image
photo = PhotoImage(file =im)                                                        #doit lier le im avec le nombre d'erreur
item = can1.create_image(200, 200, image =photo)
can1.pack(side='right', padx =10, pady =5)
#-------------------------------------------------------------------------------------------------------------------------------

buttonQuit = Button(fenetre, text="QUITTER", fg='red', command=fenetre.destroy)     #Bouton quitter
buttonQuit.pack(side='bottom', padx=5, pady=300)
#-------------------------------------------------------------------------------------------------------------------------------

fenetre.mainloop()                                                                  #lancement du gestionnaire d'évenements