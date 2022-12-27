nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]

# method one
# newnums = []
# for i in range(len(nums)):
#     newnums.insert(index[i],nums[i])
# print(newnums)

# method two
array = []
for i, j in zip(nums, index):
    array.insert(j, i)
print(array)
