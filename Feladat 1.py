def main():
    age = int(input("Kor:"))

    if age >= 21:
        print("Fogyaszthat alkoholt Amerikában")
    else:
        print("Nem fogyaszthat alkoholt Amerikában")
    
    if age >= 18:
        print("Vehet dohányterméket")
    else:
        print("Nem vehet dohányterméket")
    
    if age >= 12:
        print("Megnézheti egyedül a Shrekt 2-t")
    else:
        print("Nem nézheti meg egyedül a Shrek 2-t")
        
    


if __name__ == "__main__":
    main()