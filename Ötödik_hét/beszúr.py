def szur(x,y):
    w = input("szöveg : ")
    z = w.find(x)

    return w[:z] + y + " " + w[z:]
    
    
   

def main():
    print(szur("bögre","piros"))




if __name__ == "__main__":
    main()