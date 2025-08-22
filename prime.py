n=int(input("Enter the number :- "))
for i in range(2,n):
    if(n%i==0):
        print("The given number is not prime :) ")
        break
else:
    print("The given number is prime :) ")