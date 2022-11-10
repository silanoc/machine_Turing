#! /usr/bin/env python3
# coding: utf-8

import questionary
import turing

def lancer_le_jeu()-> None:
    print("bienvenu sur ce simulateur de machine de turing")
    print("----------------------")
    choisir_et_lancer()

def choisir_la_machine()-> str:
    choix_machine = questionary.select("Quelle machine voulez-vous utiliser ?",
                                       choices = ["doubler les un", "ajouter 1",
                                              "une autre via un fichier yaml personnalisé"]).ask()
    if choix_machine == "doubler les un":
        fichier = "doublerlesun.yaml"
    elif choix_machine == "ajouter 1":
        fichier = "ajouter1.yaml"
    else:
        print("pas ok, par défaut ajouter 1")
        fichier = "ajouter1.yaml"
    return fichier

def executer_la_machine(chemin: str)-> None:
    machine = turing.creer_une_machine_via_yaml(chemin)
    print("___affichage_initialisation___")
    print(machine.listedetat)
    print(machine.bandepapier)
    print("___affichage_fonctionnement___")
    machine.excecuter_le_programme_de_la_machine()
    voulez_vous_continuez()

def choisir_et_lancer()-> None:
    la_machine_choisie: str = choisir_la_machine()
    executer_la_machine(la_machine_choisie)

def voulez_vous_continuez()-> None:
    choix_continuer = questionary.select("voulez vous relancer une machine ou quitter",
                                         choices = ["relancer une machine",
                                                    "quitter le programme"]).ask()
    if choix_continuer == "relancer une machine":
        choisir_et_lancer()
    elif choix_continuer == "quitter le programme":
        quitter()

def quitter()-> None:
    print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
    exit()
        