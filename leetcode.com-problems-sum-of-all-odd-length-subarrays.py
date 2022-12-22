

arr = [10,11,12]
odd = 3
l = len(arr)
total = sum(arr)
print(total)
for i in range(l):
    print(odd,'oddd')
    if odd <= l:
        for j in range(l-(odd-1)):
            total = total + sum(arr[j:j+odd])
            print(total)
        odd = odd+2
    else:
        break
print(total)
