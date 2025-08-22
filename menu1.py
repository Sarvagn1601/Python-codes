while(1):
    print("\n************************")
    print("1 for centi to inch ")
    print("2 for celcius to frhanite ")
    print("3 for sec to hour,minute,sec")
    print("4 for exit")
    ch=int(input("Enter your choice : "))

    if(ch==1):
        cm=float(input("Enter the length in centimeter :- "))
        if (cm < 0):
            print("invalid input")
        else:
            inch = cm/2.54
            print("The converted cm to inch is :- ", inch)
    elif(ch==2):
        celcius=float(input("Enter The Tempreture in celcius :- "))
        f=((celcius*9/5)+32)
        print("The Ferhanite is :- ",f)
    elif(ch==3):
        sec=float(input("Enter the time in sec :- "))
        hour=sec//3600
        min=(sec%3600)//60
        sec=sec%60
        print("The time is ",hour,":",min,":",sec)
    elif(ch==4):
        break
    else:
        print("Invalid choice")
