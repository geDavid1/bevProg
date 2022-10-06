def main():
    x = input("Szöveg: ")
    x2 = ""

    for i in range(len(x)):
        x2 = x2 + chr(ord(x[i])-3)



    print(x2)               # nice RickRoll


if __name__ == "__main__":
    main()