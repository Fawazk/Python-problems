nums = [1, 2, 3, 4, 1, 5]

# method one

# newlist =[]
# for i in range(0,int(len(nums)),2):
#     print(i)
#     while nums[i]>0:
#         newlist.append(nums[i+1])
#         nums[i] = nums[i] - 1
# print(newlist)

# method two

lst = []
for freq, value in zip(nums[::2], nums[1::2]):
    lst.extend(freq * [value])

print(nums[::2], nums[1::2])
