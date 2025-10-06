#sum of 1 to n natural number 
# by paramaterized way
# def func(sum,i,n):
#     if i >n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)

# func1(0,1,4)

def func1(n):
    if n==1:
        return 1
    return n+func1(n-1)

x=func1(4)
print(x)