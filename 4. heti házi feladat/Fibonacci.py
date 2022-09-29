def rekfibo(n):
    if n==0 or n==1:                            #megálási feltétel
        return n
    else:
        return rekfibo(n-1) + rekfibo(n-2)      #rekurziv hivás





def main():
    n = int(input())
    print(n,". fibo: ",rekfibo(n))





if __name__ == "__main__":
    main()