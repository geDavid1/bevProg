def tukor(n):

    regi = n                            #bemeneti szám mentése
    uj = 0

    while n > 0:
        szj = n%10                      #számjegyekre bontás
        uj = uj*10 +szj                 #új szám lértrehozása az előző szám számjegyeiből
        n //= 10

    
    print(uj)
    if regi == uj:
        return True
    else:
        return False
    



def main():
    n = int(input())

    if tukor(n):
        print("Tukor")
    else:
        print("Nem tukor")



if __name__ == "__main__":
    main()