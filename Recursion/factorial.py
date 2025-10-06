def rec(n):
    if n==1:
        print(n)
        return
    rec(n*n-1)

rec(3)