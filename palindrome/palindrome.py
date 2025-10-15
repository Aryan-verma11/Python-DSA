#palindrome oonhy kahty hai jinhy hum aagye sy padhey ya picchy padhey same hi ho jaisy :-
# REACECAR,MOM,NITIN etc

s="ABCDCBA"  
def func(s):
    r=len(s)-1# r starts from the last index of the string
    l=0# l starts from the first index
    while l<r: # loop until both pointers meet in the middle
        if s[l]!=s[r]:# if characters at both ends don't match
            return False# it's not a palindrom
        l+=1# move left pointer forward
        r-=1 # move right pointer backward
    return True  # if loop completes, it's a palindrome
      
print(func(s))
        
print("-------------------------------")


left=0
right=len(s)-1
def func1 (s,left,right):
    if left>=right: # base case: crossed the middle
        return True
    if s[left]!=s[right]:  # characters don’t match
        return False
    return func1(s,left+1,right-1) # move inward

print(func1(s,left,right))