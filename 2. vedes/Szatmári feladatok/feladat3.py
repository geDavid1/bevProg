def sameStr(x,y) -> bool:

    sXszkm = x.replace(" ","")
    sYszkm = y.replace(" ","")
  

    
    sX = sorted(sXszkm.lower())
    sY = sorted(sYszkm.lower())
    benneVan = True

    
    
    if sX != sY:
        benneVan = False
    else:
        benneVan = True
     
    return benneVan


     


def main():
    x = input()
    y = input()

    sameStr(x,y)

    if sameStr(x,y):
        print("annag")
    else:
        print("nem annag")







if __name__ == "__main__":
    main()