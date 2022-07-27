

nums = [1,2,3,1,7]
target = 10
dict={}

# method one
for i in range(len(nums)):
    if dict.get(nums[i]) is not None:
        print(dict.get(nums[i]),i)
    else:
        dict[target - nums[i]] = i
        print(dict[target - nums[i]],"target",dict)
        
# method two
for i,n in enumerate(nums):
    print(dict)
    if n in dict:
        print(dict[nums[i]],i)
    dict[target - nums[i]] = i
    

        
# method three
for i,n in enumerate(nums):
    diff = target - n
    if diff in dict:
        print(dict[diff],i)
    else:
        print(dict)
        dict[n]=i
    