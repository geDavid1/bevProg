def nKobOsszeg():
   x = int(input("N = "))                           #első n összege
   sum = ((x*(x+1))/2)**2
   print("{:.0f}".format(sum))
   
   return 0

def nNegyzetOsszeg():
    x = int(input("N = "))                          #első n összege
    sum = (x*(x+1)*(2*x+1))/6
    print("{:.0f}".format(sum))

    return 0

def mertaniHaladvanyOsszeg():
    x = int(input("Haladvány első tagja: "))
    r = int(input("Állandó hányados: "))
    n = int(input("N = "))                           #első n összege

    
   

    if r == 1:
        sum = r*x
    else:
        sum = x*(r**n -1)/(r-1)

    print("{:.0f}".format(sum))

    return 0


def menu(x):
    match x:
        case "1":
            nKobOsszeg()
        case "2":
            nNegyzetOsszeg()
        case "3":
            mertaniHaladvanyOsszeg()
        






def main():
    
    val = input(" '1': Első n természetes szám köbösszege\n '2': Első n természetes szám négyzet összege\n '3': Mértani haladvány(sorozat)-ban lévő első n szám összege.\n  Válasszon 1,2,3:\n")  
    
    menu(val)
    
    

if __name__ == "__main__":
    main()
