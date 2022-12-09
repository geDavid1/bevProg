def main():
    
    filePy = open("barmi.txt","a")
    for i in range(10):
        print(i,file=filePy)
    filePy.close()





if __name__ == "__main__":
    main()