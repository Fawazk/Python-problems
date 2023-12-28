# method one
nums = [2, 5, 1, 3, 4, 7]
n = 3
ans = []
ptr1 = 0
ptr2 = n

for i in range(0, int(len(nums) / 2)):
    print(i, "i")
    ans.append(nums[ptr1])
    ans.append(nums[ptr2])
    ptr1 += 1
    ptr2 += 1

print(ans)


# method two
# array = []
# for i in range(n):
#     array.append(nums[i])
#     array.append(nums[i+n])
# print(array)
