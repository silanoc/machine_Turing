#! /usr/bin/env python3
# coding: utf-8

import questionary
import turing

"""interface en mode console de la machine de Turing
By silanoc, 10 novembre 2022"""

def choisir_la_machine()-> str:
    """quesionnaire pour choisir la macine à lancer"""
    choix_machine = questionary.select("Quelle machine voulez-vous utiliser ?",
                                       choices = ["doubler les un", "ajouter 1",
                                              "une autre via un fichier yaml personnalisé"]).ask()
    if choix_machine == "doubler les un":
        fichier = "doublerlesun.yaml"
    elif choix_machine == "ajouter 1":
        fichier = "ajouter1.yaml"
    else:
        fichier = proposer_un_fichier()
    return fichier

def proposer_un_fichier()-> str:
    """demande à l'utilisateur le chemin d'un fichier.
    aucun test de vérification n'est fait !
    Ce n'est pas bien, mais pour un simple test, je me l'autorise.
    todo : mettre un test d'existance du fichier
    """
    chemin = questionary.text("veuillez entre le chemin du fichier").ask()
    return chemin

def executer_la_machine(chemin: str)-> None:
    """création d'une instance de machine,
    affiche les parametre
    affiche les étapes successifs
    """
    machine = turing.creer_une_machine_via_yaml(chemin)
    print("___affichage_initialisation___")
    print(machine.listedetat)
    print(machine.bandepapier)
    print("___affichage_fonctionnement___")
    machine.excecuter_le_programme_de_la_machine()
    voulez_vous_continuez()

def choisir_et_lancer()-> None:
    """simple combinaison pour éviter un doublon de code"""
    la_machine_choisie: str = choisir_la_machine()
    executer_la_machine(la_machine_choisie)

def voulez_vous_continuez()-> None:
    """questionnaire pour continuer ou quitter"""
    choix_continuer = questionary.select("voulez vous relancer une machine ou quitter",
                                         choices = ["relancer une machine",
                                                    "quitter le programme"]).ask()
    if choix_continuer == "relancer une machine":
        choisir_et_lancer()
    elif choix_continuer == "quitter le programme":
        quitter()

def lancer_le_jeu()-> None:
    """le début du programme"""
    print("bienvenu sur ce simulateur de machine de turing")
    print("----------------------")
    choisir_et_lancer()

def quitter()-> None:
    """pour quitter proprement le programme"""
    print("Merci d'avoir utilisé mon programme. A une prochaine fois.")
    exit()


if __name__ == "__main__":
    lancer_le_jeu()
        