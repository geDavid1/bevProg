def szur(x,y):
    w = input("Változtandó szöveg : ")
    z = w.find(x)

    return w[:z] + y + " " + w[z:]
    
    
   

def main():
    x = input("Szöveg 1. :")
    y = input("Szöveg 2. :")
    print(szur(x,y))
    




if __name__ == "__main__":
    main()
