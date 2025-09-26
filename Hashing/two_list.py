# it tells thge number of repetitions in two lists
n=[7,9,8,7,6,4,9,2,3,4,1,]
m=[2,4,5,7,5,7,8,9,5,6,4,6]
for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
    print(count)
