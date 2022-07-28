# method one

# from collections import OrderedDict

s="codeleet"
indices=[4,5,6,7,0,2,1,3]

fname = ""
dictvalue2={}
dictvalue = dict(zip(indices,s))
for j in sorted(dictvalue):
    dictvalue2[j] = dictvalue[j]
# dictvalue2=OrderedDict(sorted(dictvalue.items()))
dictvalue = list(dictvalue2.values())
for i in dictvalue:
    fname += i
print(fname)

# method two
combo = [(i,j) for i,j in zip(s,indices)] #list of tuples
print(combo)
combo.sort(key=lambda c:c[1]) #sort on the inexes
print("".join([i for i,j in combo])) #return string from sorted list of tuples.

# method three

arr=[None]*len(s)
s1=""
for i in range(0,len(indices)):
    # arr.insert(indices[i],s[i])
    arr[indices[i]]=s[i]
for elem in arr:
    s1+=elem
print(s1)