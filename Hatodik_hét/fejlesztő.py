class fejleszto():
    def __init__(self,nev,fiz,ev =0) -> None:
        self.nev = nev
        self.rang = "Junior"
        self.ev = ev
        self.fiz = fiz


    def fizEm(self,fiz=10000):                  #alapértelmezetten +10k
        self.fiz += fiz


    def evEm(self):
        self.ev += 1

    def rangEl(self,ev):

        match self.ev:
            case self.ev if self.ev == 0:
                self.rang = "Intern"
            case self.ev if 1 <= self.ev <= 2:
                self.rang = "Junior"
            case self.ev if 2 <= self.ev <= 5:
                self.rang = "Medior"
            case self.ev if self.ev > 5:
                self.rang = "Senior"

   
    def ki(self):
        print("Nev: {0}, Rang: {1}, Fizetés: {2}, Ledolgozott évek: {3}".format(self.nev,self.rang,self.fiz,self.ev))
    
   




def main():
    pass


if __name__ == "__main__":
    main()
