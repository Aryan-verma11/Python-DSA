#armstrong no. lets suppose a numnber 153 so if we take cube of 1 + cube of 5 + cube of 3 so, 1+125+27 =153 so its a armostring number.
# yaha cube isliye kiya kiuki 3 number thy agr 2 number hoty to square krty aur 4 hoty to power 4 hoti
n=153
num=n
nod=len(str(num))
total=0
while num>0:
    ld=num%10
    total=total+(ld**nod)
    num=num//10
if n==total:
    print("an armstrong number")
else:
    print("not armstrong")
    