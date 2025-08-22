while(1):
    print("\n**********************")
    print("1 for area of square")
    print("2 for area of Rectangle")
    print("3 for area of Circle")
    print("4 for area of Triangle")
    print("5 for Exit")
    ch=int(input("What Your choice"))

    if(ch==1):
        l=float(input("Enter L= "))
        area=l*l
        print("Area = ",area)
    elif(ch==2):
        l=float(input("Enter L= "))
        B=float(input("Enter B= "))
        area=l*B
        print("Area = ",area)
    elif(ch==3):
        r=float(input("Enter r= "))
        area=3.14*r*r
        print("Area = ",area)
    elif(ch==4):
        l=float(input("Enter L= "))
        h=float(input("Enter H= "))
        area=1/2*l*h
        print("Area = ",area)
    elif(ch==5):
        break
    else:
        print("Invalid choice")