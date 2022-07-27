
nums = [0,2,1,5,3,4]
ans = []
for i,n in enumerate(nums):
    ans.append(nums[nums[i]])

# method two
ans = [nums[i] for i in nums]
print(ans)