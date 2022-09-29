import math


def Tkor(r):
    return (r**2)*math.pi

def Ttegla(x,y):
    return x*y

def Tgulakup(t,m):
    return (t*m)/3

def menu(x):
    match x:
        case "g":
            x = int(input("Alap hossza: "))
            y = int(input("Alap szélessége: "))
            m = int(input("Gúla magassága: "))
            tt=Ttegla(x,y)
            
            print("Gúla térfogata: ", "{:.2f}".format(Tgulakup(tt,m)))
        
        case "k":
             r = int(input("Kör sugara: "))
             m = int(input("Kúp magassága: "))
             tk=Tkor(r)
             print("Kúp térfogata: ", "{:.2f}".format(Tgulakup(tk,m)))



def main():
    
    val =input("Gulának vagy kúpnak szeretná a térfogatát kiszámitani: g/k \n")
    menu(val)


if __name__ == "__main__":
    main()