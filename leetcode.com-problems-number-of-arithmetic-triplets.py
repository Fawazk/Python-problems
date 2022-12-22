nums = [4,6,5,7,8,9]
diff = 2
count = 0
t = []


for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[j] - nums[i] == diff:
            for k in range(j+1,len(nums)):
                if nums[k] - nums[j] == diff:
                    t.append((i,j,k))
                    count += 1
print(count)
print(t)    