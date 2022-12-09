def main():
    fileP = open('pivers.txt', 'w') 
    tmp="How I want a drink alcoholic of course After the heavy lectures involving complex functions"
    print(tmp, file=fileP) 
    
    
    with open('pivers.txt', 'r') as fileP, open('piSzam', 'w') as filepSz: 
        tmp=fileP.read()  
        tmpL=tmp.split(sep=' ') 

        print(len(tmpL[0]), file=filepSz)
    
    
    fileP.close()
    filepSz.close()
    
if __name__=="__main__":
    main()