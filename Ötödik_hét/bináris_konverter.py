def main():
    x = int(input("Szám: "))
    m=""
    while x != 0:
        m = m + str(x % 2)
        x //=2

    print(m[::-1])
 


if __name__ == "__main__":
    main()
