# suppose we have list=[1,1,1,1,1,2,2,2,2,3,3,3,3] auer ab ismy hmmey iski frequency likhni hai to hum oos dict me key:value pair likhengy key me 1 aur value me 1 kitni bar aa rha hai jai 
# jaisy {1:5,2:4,3:4}
# num=[2,2,2,2,4,4,5,2,2,2,2,1,1,1,1,1,8,8,8,8]
# frequency_map={}
# for i in range(0,len(num)):
#     if num[i] in frequency_map:
#         frequency_map[num[i]]+=1
#     else:
#         frequency_map[num[i]]=1
# print(frequency_map)


# tc=O(n)
# sc=O(n)



# .get func hmmey automatically bata detab hai ki oos num ki value kya hau kitni baar ayah hai aur kitni ooski frquency hai

nums=[2,2,2,2,4,4,5,2,2,2,2,1,1,1,1,1,8,8,8,8]
hash_map={}
n=len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)