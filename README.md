# Machine de Turing
- Autair : Silanoc
- Date : 
    - V0 : 3 mai 2021
    - V1.0 : 25 octobre 2022
    - V1.1 : 10 novembre 2022
- Programme simulant le fonctionnement d'une machine de Turing.
    - La V0 a été faite avant ma formation, la V1 après. il sagit du fichier "turing-test1.py"

## Requierements
PyYAML - pour lire les fichiers .yaml
Questionary - pour demander les choix de navigation dans la console
l'installation se fait avec 
`pip install -r requierements.txt` 

## Utilisation
Lancer le programme avec :
`python3 run.py`

Il faut choisir la machine que l'on veut.

Il y en a deux à titre de démonstration . Si on veut changer le contenu de la bande il faut modifier le fichier yaml concerné.

On peut importer une machine personnalisé à partir d'un fichier yaml. Attention de bien respecter la syntaxe des fichiers de démonstration"

## Fonctionnement
- La description vient de wikipédia : https://fr.wikipedia.org/wiki/Machine_de_Turing
- l'initialisation de doublerlesun.yaml aussi

- le fichier ajouter1.yaml vient du site https://interstices.info/comment-fonctionne-une-machine-de-turing/
Mais il faut intervertir gauche et droite.

## TODO 
- vérifier l'existance des fichiers personnalisé
- rendre le contenu de la bande de papier personnalisable dans la console, sans à avoir à modifier le yaml