# test machine turing

class machineturing:
    pass
    def __init__(self,Q,gamma,q0,delta,F,bande,debut):
        self.listedetat=Q
        self.alphabet=gamma
        self.etatinitial=q0
        self.fonctiontransmission=delta
        self.etatfinaux=F
        self.bandepapier=bande
        self.positioncurceur=debut
    def lecture_case(self):
        return self.bandepapier[self.positioncurceur]
    def ecriture_case(self,valeur):
        self.bandepapier[self.positioncurceur]=valeur
    def droite(self):
        self.positioncurceur+=1
    def gauche(self):
        self.positioncurceur-=1
    def change_etat(self,valeur):
        self.etat=valeur
    def fait_tout(self):
        print("az")
        self.etat=self.etatinitial
        while self.etat !="arret":
            self.symbole_lu=self.lecture_case()
            print(self.etat, self.symbole_lu, self.positioncurceur)
            if self.etat=='e1' and self.symbole_lu==0:
                self.etat='arret'
            elif self.etat=='e1' and self.symbole_lu==1:
                self.ecriture_case(0)
                self.droite()
                self.change_etat('e2')
            elif self.etat=='e2' and self.symbole_lu==1:
                self.ecriture_case(1)
                self.droite()
                self.change_etat('e2')
            elif self.etat=='e2' and self.symbole_lu==0:
                self.ecriture_case(0)
                self.droite()
                self.change_etat('e3')
            elif self.etat=='e3' and self.symbole_lu==1:
                self.ecriture_case(1)
                self.droite()
                self.change_etat('e3')
            elif self.etat=='e3' and self.symbole_lu==0:
                self.ecriture_case(1)
                self.gauche()
                self.change_etat('e4')
            elif self.etat=='e4' and self.symbole_lu==1:
                self.ecriture_case(1)
                self.gauche()
                self.change_etat('e4')
            elif self.etat=='e4' and self.symbole_lu==0:
                self.ecriture_case(0)
                self.gauche()
                self.change_etat('e5')
            elif self.etat=='e5' and self.symbole_lu==1:
                self.ecriture_case(1)
                self.gauche()
                self.change_etat('e5')
            elif self.etat=='e5' and self.symbole_lu==0:
                self.ecriture_case(1)
                self.droite()
                self.change_etat('e1')
            print(self.bandepapier)

    #def aggrandi le ruband
    #def initialise le ruband

def doublerlesUn():
    etats=['e1','e2','e3','e4','e5'] #état initial est e1
    alphabet=[0,1] #‘0’ étant le « symbole blanc »
    etatinit='e1'
    delta=''
    etatsfin=''
    #bande=[1,1,1,1,1,1,1,1,1,1]
    bande=[1,1,1,1,0,0,0,0,0,0]
    debut=0
    return machineturing(etats,alphabet,etatinit,delta,etatsfin,bande,debut)
   
machine=doublerlesUn()
print (machine.listedetat)
print(machine.bandepapier)
machine.fait_tout()