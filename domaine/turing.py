#! /usr/bin/env python3
# coding: utf-8

"""Simultion d'une machine de Turing
By Silanoc le 25 octobre 2022
"""

from typing import Tuple
import yaml

class Machineturing:
    """La classe qui gére le fonctionnement d'une machine de turing"""

    def __init__(self, Q, gamma, q0, delta, F, bande, debut, tabledeverite, symbole_blanc):
        assert symbole_blanc in gamma
        self.listedetat: list = Q
        self.alphabet: list = gamma
        self.etatinitial: str = q0
        self.fonctiontransmission = delta
        self.etatfinaux = F
        self.bandepapier: list = bande
        self.positioncurceur: int = debut
        self.tabledeverite: dict = tabledeverite
        self.symbole_blanc: str = symbole_blanc

    def lecture_case(self) -> str:
        "Lit le contenu de la case sous le curseur. Retour un str"
        return self.bandepapier[self.positioncurceur]

    def ecriture_case(self,valeur: str) -> None:
        "Ecrit le valeur (si existe dans alphabet) dans la case de la bandepapier"
        assert valeur in self.alphabet
        self.bandepapier[self.positioncurceur] = valeur

    def droite(self)-> None:
        "déplace le curseur d'une case vers la droite en ajoutant une case si nécessaire"
        self.positioncurceur += 1
        if self.positioncurceur == len(self.bandepapier):
            self.bandepapier.append(self.symbole_blanc)

    def gauche(self)-> None:
        "déplace le curseur d'une case vers la gauche en ajoutant une case si nécessaire"
        self.positioncurceur -= 1
        if self.positioncurceur < 0:
            self.bandepapier.insert(0, self.symbole_blanc)

    def change_etat(self, valeur1: str)-> None:
        "change l'état de la machine"
        self.etat = valeur1

    def definir_tuple_entree_transition(self)-> Tuple[str, str]:
        "Construction du tuple état et symbole lu"
        tuple_sortie: Tuple[str, str] = (self.etat, self.lecture_case())
        return tuple_sortie

    def fonction_de_transition(self, tuple_entree)-> None:
        "execute les instruction de la table de transition en fonction du tuple d'entree"
        try:
            instruction_a_faire: list[str, str, str] = self.tabledeverite[f"('{tuple_entree[0]}','{tuple_entree[1]}')"]
            print(instruction_a_faire)
            self.ecriture_case(instruction_a_faire[0])
            if instruction_a_faire[1] == 'droite':
                self.droite()
            elif instruction_a_faire[1] == 'gauche':
                self.gauche()
            self.change_etat(instruction_a_faire[2])
        except:
            self.etat = 'arret'
            print("arret")

    def excecuter_le_programme_de_la_machine(self) -> None:
        """execute les instructions jusqu'à l'état de fin, arret"""
        self.etat = self.etatinitial
        while self.etat != 'arret':
            parametre_entree = self.definir_tuple_entree_transition()
            print(parametre_entree, self.positioncurceur)
            self.fonction_de_transition(parametre_entree)
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
        elif key == "symbole_blanc":
            symbole_blanc = value
    return Machineturing(etats, alphabet, etatinit, delta, etatsfin, bande, debut, tabledeverite, symbole_blanc)

if __name__ == "__main__":
    machine = creer_une_machine_via_yaml("doublerlesun.yaml")
    print("___affichage_initialisation___")
    print(machine.listedetat)
    print(machine.bandepapier)
    print("___affichage_fonctionnement___")
    machine.excecuter_le_programme_de_la_machine()
    print('############')
    machine = creer_une_machine_via_yaml("ajouter1.yaml")
    print("___affichage_initialisation___")
    print(machine.listedetat)
    print(machine.bandepapier)
    print("___affichage_fonctionnement___")
    machine.excecuter_le_programme_de_la_machine()
