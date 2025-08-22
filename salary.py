salary=float(input("Enter your salary :- "))

hra=salary*0.45
da=salary*0.09
pf=salary*0.1
tax=salary*0.12
netpay=salary+hra-da-pf-tax

print("Hra is ",hra)
print("DA is ",da)
print("Pf is ",pf)
print("Tax is ",tax)
print("Net Pay is ",netpay)