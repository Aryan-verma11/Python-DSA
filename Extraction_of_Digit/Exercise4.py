# Palindrome:-wo value jisko oolta padhny pe bhi same hi aaye oosy palindrome kahty hai jaisy 
#nitin ko oolta padhny pe nitin hi aata hai 
#we can also do this by string but that is not the correct way

n=11224221134
num=n
result=0
while num>0:
    ld=num%10
    result=(result*10)+ld
    num=num//10
if n==result:
    print("The number is palindrome: ")
else:
    print("The number is not a palindrome")

# tc=log10(n)