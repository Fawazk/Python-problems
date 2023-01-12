# Find the next largest number with the same digits.
# Example 1:
# Input: 123321
# Output: 131223

# Input= 123321
Input = int(input("Enter a number"))
num = list(map(int, str(Input)))
leng = len(num)
l = len(num)-1
l2 = len(num)-2
temp = 0
flag = False
for i in range(leng-1):
    if num[l] > num[l2]:
        temp = num[l2]
        num[l2]=num[l]
        num[l] = temp
        flag = True
        break
    
    l = l-1
    l2 = l2-1
if flag:
    next = sorted(num[l:leng])
    result = num[0:l] + next
    result = int("".join(map(str, result)))
    print(result)
else:
    print(Input)