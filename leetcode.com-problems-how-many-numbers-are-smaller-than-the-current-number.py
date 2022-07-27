

nums=[8,1,2,2,3]
# method one
# new = []
# for i in range(len(nums)):
#     count = 0
#     for j in range(len(nums)):
#         print(i)
#         if nums[i] > nums[j]:
#             count = count +1
#         else:
#             pass
#     new.append(count)
# print(new)

# method two
print(sorted(nums).index(i) for i in nums)