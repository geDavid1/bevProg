def nyomtato(x) -> list:
    szamLista = []

    y=x.split(sep=",")

    for i in y:
        intervallum=False 
        for j in i: 
            if (j=="-"): 
                intervallum=True 
        if intervallum==True: 
            szamOLista=i.split(sep='-') 
            n=int(szamOLista[0]) 
            szamLista.append(n)
            while True: 
                n=n+1 
                szamLista.append(n)
                if n==int(szamOLista[1]): 
                    break  
        elif intervallum==False:
             szamLista.append(int(i))
        
        
        
    return szamLista


def main():
    x=input()

    

    print(nyomtato(x))


if __name__=="__main__":
    main()