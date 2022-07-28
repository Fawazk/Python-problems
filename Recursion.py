def Recursion(n):
    print(n)
    if n<=1:
        return n
    else:
        return n + Recursion(n-1)
s=Recursion(10)
print(s)