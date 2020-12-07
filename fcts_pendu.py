#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:37:37 2020
@author: amandine

Le jeu du pendu

"""

#IMPORTATION BIBLIOTHEQUES
import random


#FONCTIONS
def TextListe ():                   #Permet de transformer le texte en liste de mots
    fich=open ('mots.txt','r')
    mots=fich.read()
    txtList = mots.split(', ')
    triTxt = sorted(txtList)        #Retourne la liste de mots
    return (triTxt)
    fich.close

    
def ChoixMot ():                    #Permet de choisir un mot dans la liste au hasard
    L=TextListe()
    rn=random.randint(1, len(L)-1)
    Valren=L[rn]
    return (Valren)                 #SORTIE : un mot au hasard


def CacheMot (Mot):                #ENTRE : mot à découvert
    Valren=Mot[0]                   #Permet d'afficher le mot caché avec les tirets et les lettres trouvées
    for i in range (len(Mot)-1):            
        Valren = Valren +'_'
    return Valren                   #SORTIE : mot caché


def Changement (Mot, Mcache, Erreur, ListeFait):        #ENTRES : Mot à découvert / Mot caché / Le nombre d'erreurs /
    lettre=input('Choissisez une lettre: \n')                     #La chaîne de caractère des lettres déjà utilisés
    if lettre in ListeFait:
        return Mcache,Erreur,ListeFait                  #Permet de remplacer la lettre trouvé dans le mot caché 
    ListeFait=ListeFait+lettre                          #ou de compté une erreur si la lettre est fausse
    if lettre in Mot:
        for i in range (len(Mot)):   
            if str(lettre)==Mot[i]:
                Mcache=Mcache[0:i]+lettre+Mcache[i+1:len(Mcache)]        
    else:
        Erreur=Erreur+1
    return Mcache,Erreur,ListeFait                      #SORTIES : Mot caché / Nb d'erreur / Chaîne de lettres fausses
    

def Affichage (Mot, Mcache, Erreur, ListeFait):         #ENTRES : même que pour la fct Changement
    L=["","| \n| \n---------","| \n| \n| \n| \n---------","|/ \n| \n| \n| \n| \n---------",
       "______ \n|/ \n| \n| \n| \n| \n---------","______ \n|/   | \n| \n| \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|  \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n| \n| \n---------",
       "______ \n|/   | \n|    o \n|   /|\ \n|   / \ \n| \n---------"]
    print (L[Erreur])
    print (Mcache)
    if Erreur==8:                                       #Permet d'afficher un pendu et de terminer le jeu
        print('Perdu')
    elif Mot==Mcache:
        print('Gagné')                                  #SORTIE : Affichage de gagner ou perdu
        

def Score(Erreur,Score):                                #ENTRES : Nb d'erreur / Meilleur score du joueur
    if Erreur<Score:                                    #Permet de calculer un nouveau score pour le joueur
        Score=Erreur
    return Score
        

def Jouer ():                                           #Permet de lancer le jeu et de deviner les lettres plusieurs fois
    r=1                                                 #en appelant toutes les fonctions.
    S=10
    while r==1:
        mot = ChoixMot()
        MotCaché = CacheMot (mot)
        LE=''
        E=0
        Affichage(mot,MotCaché,E,LE)
        while E<8 and mot!=MotCaché:
            MotCaché,E,LE=Changement(mot, MotCaché, E, LE)
            Affichage (mot, MotCaché, E, LE)
        S=Score(E,S)
        print('Votre nombre de derreurs est : '+ str(E))
        print('Votre meilleur score est : '+ str(S))
        r=int(input('Voulez-vous jouer? (1 ou 0) : \n'))
    
