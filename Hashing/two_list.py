# it tells the number of repetitions in both the lists ki m list me jo bhi number hai wo wo check krega n list me aur agr wahi number dono me hua to + 1 ho jayega aur bateyga ki ye number dno me  1 baar repeat hua hai 
# n=[7,9,8,7,6,4,9,2,3,4,1,]
# m=[2,4,5,7,5,7,8,9,5,6,4,6]
# for num in m:
#     count=0
#     for x in n:
#         if x==num:
#             count+=1
#     print(count)
# this the program for aam zindagi 

# tc=O(n|sq.)

# let me depict you a mentos zindagi code for this

n=[7,9,8,7,6,4,9,2,2,2,1,]
m=[2,4,5,7,5,7,8,9,5,6,4,6]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
    for num in m:
        if num<1 or num>10:
            print(0)
        else:
            print(hash_list[num])