nums=[4,6,3,7,4,8,9,65,33,6,7,8]
nums.reverse()
nums[::-1]
print(nums)
#by concept of pointer in python
num1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l=0
r=len(num1)-1
while l>r:
    num1[l],num1[r]=num1[r],num1[l]
    l+=1
    r-=1
print(num1)