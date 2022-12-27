nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
# method one

# n = len(nums)
# i=0
# while(i<n):
#     if nums[i] == val:
#         # nums[i] = nums[n-1]
#         nums.pop(i)
#         print(nums,'==',i)
#         n = n-1
#     else:
#         i +=1
# print(nums,'lastone')
# print(nums)

# method two
# x=0
# for i in range(len(nums)):
#     if nums[i]!=val:
#         nums[x]=nums[i]
#         x+=1
# return x

length = len(nums)
i = 0
while i < length:
    if nums[i] == val:
        nums.pop(i)
        i = -1
    else:
        i = +1
print(nums)
