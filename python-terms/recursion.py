def Recursion(n):
    if n <= 1:
        return n
    else:
        return n + Recursion(n - 1)


print(Recursion(int(input("Enter a number :"))))
