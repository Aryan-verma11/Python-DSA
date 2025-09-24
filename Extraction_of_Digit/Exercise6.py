#print all factors of given number in the list
n=36
num=n
# result=[]
# for i in range(1,num+1):
#     if num%i==0:
#         result.append(i)
# print(result) 

#tc=O(n)
#sc=O(k)jitny factor hongy




# agar hum dhyan de to hmmey pta chlega hum apny for loop ko adhy tk le kr ja skty hai kiuki 10 ke factor 1 hoga 2 hoga 5hoga fir sidha 10 khud hoga to : for better time complexity we can run our for loop till half

result1=[]
for i in range(1,num//2):
    if num%i==0:
        result1.append(i)
print(result1) 

# tc=O(n/2) similar to O(n)
# sc=O(k)jitny factor hongy



from math import sqrt
result2=[]
for i in range(1,int(sqrt(num))+1):
    if num%i==0:
        result2.append(i)
        if (num//i !=i):
            result2.append(num//i)
print(result2) 