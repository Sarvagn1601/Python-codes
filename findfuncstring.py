#find length,count,numberofalpha,digit,uppercase,lowercase,space and vowels from string
str=input("Enter the string :- ")
#count=0
alpha=0
digit=0
upper=0
lower=0
space=0
vowel=0
le=0

for i in str:
    le=le+1
print("The length of string is ",le)

for i in str:
    if(i.isalpha()):
        alpha=alpha+1
print("Total alphabet is ",alpha)

for i in str:
    if(i.isdigit()):
        digit=digit+1
print("Total Digit is ",digit)

for i in str:
    if(i.isupper()):
        upper=upper+1
print("Total uppercase is ",upper)

for i in str:
    if(i.islower()):
        lower=lower+1
print("Total lowercase is ",lower)

for i in str:
    if(i.isspace()):
        space=space+1
print("Total space is ",space)

for i in str:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U"):
        vowel=vowel+1
print("Total Vowel is ",vowel)