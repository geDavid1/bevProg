def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    x =""

    for i in range(len(text)):
        for z in chars:
            if text[i] == z:
                x += z
    return x



def main():
    valid("Barking!")
    valid("KL754", "0123456789")
    valid("BEAN", "abcdefghijklmnopqrstuvwxyz")




if __name__ == "__main__":
    main()