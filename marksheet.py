sub1= int(input("Enter the Marks of subject 1 :- "))
sub2= int(input("Enter the Marks of subject 2 :- "))
sub3= int(input("Enter the marks of subject 3 :- "))

total= sub1+sub2+sub3

per= total/3

print("The total marks of your all subject is ",total,"/300")
print("The percentage is ",per)

if(sub1>=40 and sub2>=40 and sub3>=40):
    if(per>= 80 ):
        print("Distinction")
    elif(per>=60):
        print("First class")
    elif(per>=40):
      print("Second Class")
else:
      print("Fail")














      