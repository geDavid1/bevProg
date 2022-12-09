def main():
    inputTxt= input()

    outputTxt = ""
    for i in inputTxt:
        tmpL = i.isalpha() 
        if tmpL==True: 
            upperL = i.isupper() 
            if upperL == True: 
                l=i.lower() 
            elif upperL == False: 
                l=i 
            n=ord(l) 
            n=n+2 
            if (n>122): 
                m=n-122 
                m=65+(m-1) 
                k=chr(m) 
                if upperL == False: 
                    outputTxt+=k 
                elif upperL == True:
                    k=k.upper() 
                    outputTxt+=k 
            elif (n<122): 
                m=n
                k=chr(m)
                if upperL == False: 
                    outputTxt+=k
                elif upperL == True:
                    k=k.upper()
                    outputTxt+=k
        else:
            outputTxt+=i
            tmpL=True
    
    tmpL=outputTxt.splitlines() 
    
    txtVeg="" 
    
    for i in tmpL: 
        try: 
            if i[0]==" ": 
                txtVeg+=i[4:len(i)] 
                txtVeg+="\n"
        except IndexError: 
            txtVeg+="\n" 
        
    print(txtVeg) 
    
if __name__=="__main__":
    main()