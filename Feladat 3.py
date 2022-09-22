

def main():
    na = int(input("Na: "))
    cl = int(input("Cl: "))

    excessNA = 0
    excessCL = 0


    finalNacl=0

    if na == 2 * cl:
        finalNacl = cl * 2
    elif na > 2 * cl:
        finalNacl = 2 * cl
        excessNA = (na - cl * 2) * 2
    else:
        finalNacl =  na
        excessCL = cl * 2 -na
    
    print("NaCl: ",finalNacl,"\n","Nátrium többlet: ",excessNA,"\n","Klór többlet: ",excessCL,"\n")


if __name__ == "__main__":
    main()