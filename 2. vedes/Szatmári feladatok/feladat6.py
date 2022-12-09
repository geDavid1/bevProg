def felhokarc(lista) ->int:
    sum = 0

    for i in range(len(lista)-1):
        if lista[i+1] > lista[i]:
            sum = sum + (lista[i+1] - lista[i])
            print(sum)
        elif i > 1:
            sum = sum + (lista[i] - lista[i-1])
            print(sum)

    return sum



def main():
    pass


if __name__ == "__main__":
    main()