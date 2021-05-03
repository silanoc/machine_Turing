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
    #def lecture case
    #def exriture case
    #def deplacement
    #def xmchangement etat 
    #def fait tout 
    #def aggrandi le ruband
    #def initialise le ruband

def doublerlesUn():
    etats=['e1','e2','e3','e4','e5'] #état initial est e1
    alphabet=[0,1] #‘0’ étant le « symbole blanc »
    etatinit='e1'
    delta=''
    etatsfin=''
    bande=[1,1,1,1,1,1,1,1,1,1]
    debut=0
    return machineturing(etats,alphabet,etatinit,delta,etatsfin,bande,debut)
   


machine=doublerlesUn()
print (machine.listedetat)