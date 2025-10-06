def rec(n):
    if n==1:
        return 1
    return n*rec(n-1)
        

x=rec(3)
print(x)

#factorial using recursion