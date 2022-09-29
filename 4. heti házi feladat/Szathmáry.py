import math


def tavolsag(a,b):
    #(x1,y1) = a     "a" pont koordinátái = a[0],a[1]
    #(x2,y2) = b     "b" pont koordinátái = b[0],b[1]
    return math.sqrt((b[1]-a[1])**2+(b[0]-a[0])**2)



def main():
    
    pont1 = (int(input()),int(input()))          # első pontnak az (x,y) koordinátái
    pont2 = (int(input()),int(input()))          # második pontnak az (x,y) koordinátái

    
    print("Távolság: ","{:.2f}".format(tavolsag(pont1,pont2)))
    
    

if __name__ == "__main__":
    main()