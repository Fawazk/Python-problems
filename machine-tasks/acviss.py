# # Find the next largest number with the same digits.
# # Example 1:
# # Input: 123321
# # Output: 131223

# example 2:
# Input : 192
# Output : 219

Input = int(input("Enter a number :"))
num = list(map(int, str(Input)))
leng = len(num)
l = len(num) - 1
l2 = len(num) - 2
temp = 0
flag = False
count = 0
first = num[0]
for i in range(leng - 1):
    if num[l] > num[l2]:
        temp = num[l2]
        num[l2] = num[l]
        num[l] = temp
        flag = True
        break
    l = l - 1
    l2 = l2 - 1
if flag and l != 1:
    print(num[l:leng])
    next = sorted(num[l:leng])
    result = num[0:l] + next
    result = int("".join(map(str, result)))
    print(result)
elif flag and l == 1:
    result = num[0:l] + num[l:leng]
    for i in range(first+1,9):
        count += 1
        if i in result:
            print(i,count)
            result.remove(i)
            temp=result[0]
            result[0]=i
            break
    result.append(temp)
    next = sorted(result[1:len(result)])
    next.insert(0,result[0])
    result = int("".join(map(str, next)))
    print(result)
else:
    print(Input)
