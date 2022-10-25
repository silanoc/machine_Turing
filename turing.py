#! /usr/bin/env python3
# coding: utf-8

"""Simultion d'une machine de Turing
By Silanoc le 25 octobre 2022
"""

import yaml

class Machineturing:
    """La classe qui gére le fonctionnement d'une machine de turing"""

    def __init__(self, Q, gamma, q0, delta, F, bande, debut, tabledeverite, ajout):
        self.listedetat: list = Q
        self.alphabet: list = gamma
        self.etatinitial: str = q0
        self.fonctiontransmission = delta
        self.etatfinaux = F
        self.bandepapier: list = bande
        self.positioncurceur: int = debut
        self.tabledeverite: dict = tabledeverite
        self.ajout: str = ajout

    def lecture_case(self) -> str:
        "Lit le contenu de la case sous le curseur. Retour un str"
        return self.bandepapier[self.positioncurceur]

    def ecriture_case(self,valeur: str) -> None:
        "Ecrit le valeur (si existe dans alphabet) dans la case de la bandepapier"
        assert valeur in self.alphabet
        self.bandepapier[self.positioncurceur] = valeur

    def droite(self)-> None:
        "déplace le curseur d'une case vers la droite"
        self.positioncurceur += 1
        if self.positioncurceur == len(self.bandepapier):
            self.bandepapier.append(self.ajout)

    def gauche(self)-> None:
        "déplace le curseur d'une case vers la gauche"
        self.positioncurceur -= 1
        if self.positioncurceur < 0:
            self.bandepapier.insert(0, self.ajout)

    def change_etat(self, valeur1: str)-> None:
        "change l'état de la machine"
        self.etat = valeur1

    def excecuter_le_programme_de_la_machine(self) -> None:
        """execute les instructions jusqu'à l'état de fin, arret"""
        self.etat = self.etatinitial
        while self.etat != 'arret':
            self.symbole_lu = self.lecture_case()
            print(self.etat, self.symbole_lu, self.positioncurceur)
            instruction_a_faire: str = self.tabledeverite[f"('{self.etat}','{self.symbole_lu}')"]
            exec(instruction_a_faire) #fonction native de python
            #print(instruction_a_faire)
            print(self.bandepapier)


def creer_une_machine_via_yaml(fichier):
    """Ouvrir le fichier yaml
    Mettre les valeurs des key:value dans les variables à utiliser
    création d'une instance de Machineturing
    """
    try:
        yaml_file = open(fichier, 'r')
        yaml_content = yaml.safe_load(yaml_file)
    except:
        print("le fichier ne c'est pas ouvert")

    print("Key: Value")
    for key, value in yaml_content.items():
        print(f"{key}: {value}")
        if key == "etats":
            etats = value
        elif key == "alphabet":
            alphabet = value
        elif key == "etatinit":
            etatinit = value
        elif key == "delta":
            delta = value
        elif key == "etatsfin":
            etatsfin = value
        elif key == "bande":
            bande = value
        elif key == "debut":
            debut = value
        elif key == "tabledeverite":
            tabledeverite = value
        elif key == "ajout":
            ajout = value
    return Machineturing(etats, alphabet, etatinit, delta, etatsfin, bande, debut, tabledeverite, ajout)

if __name__ == "__main__":
    machine = creer_une_machine_via_yaml("doublerlesun.yaml")
    #machine = creer_une_machine_via_yaml("ajouter1.yaml")
    print("___affichage_initialisation___")
    print(machine.listedetat)
    print(machine.bandepapier)
    print("___affichage_fonctionnement___")
    machine.excecuter_le_programme_de_la_machine()
    