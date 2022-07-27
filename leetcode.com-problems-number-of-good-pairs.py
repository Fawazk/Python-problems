

nums=[1,2,3,1,1,3,1]
# method one
d = {}
count = 0
for i in nums:
    d[i] = d.get(i, 0)+1
for key, value in d.items():
    print(d.items())
    if value > 1:
        ans =  (value*(value-1))/2
        count +=ans
print(count)


# method two
key=[]
value=[]
dict = []
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i] == nums[j] and i<j:
            key.append(i)
            value.append(j)
            
dict=list(zip(key,value))        
print(len(dict))