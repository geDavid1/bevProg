def main():
    with open("string1.py","r") as fileI, open("string_clean.py","w") as fileO:
        tmp = fileI.readline()

        for sorok in tmp:
            for sorokI in sorok:
                if sorokI != "#":
                    print(sorokI,file=fileO)








if __name__ == "__main__":
    main()