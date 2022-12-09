import random

def szJatek():
    rSzam = random.randint(1,100)

    db = 0

    fut = True
    while fut:
        db +=1
        szam = int(input())
        if szam == rSzam:
            print("Eltaláltad ",db,"db probálkozásból")
            fut = False
        elif szam < rSzam:
            print("Nagyobb")
        else:
            print("Kisebb")


def main():
    szJatek()    
    




if __name__ == "__main__":
    main()