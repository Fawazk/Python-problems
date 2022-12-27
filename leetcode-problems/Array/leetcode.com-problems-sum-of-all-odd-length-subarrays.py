

arr = [10,11,12]
odd = 3
l = len(arr)
total = sum(arr)
print(total)
# for i in range(l):
#     print(odd,'oddd')
#     if odd <= l:
#         for j in range(l-(odd-1)):
#             total = total + sum(arr[j:j+odd])
#             print(total)
#         odd = odd+2
#     else:
#         break
# print(total)

# j = 0
# while odd<=l:
#     print(total,'1')
#     if j <= l-odd:
#         total = total + sum(arr[j:j+odd])
#         print(total,'2')
#         j = j+1
#     else:
#         j=0
#         odd = odd+2
# print(total)


#  leetcode solution
total = 0; freq = 0; n = len(arr)
for i in range(n):
    freq = freq-(i+1)//2+(n-i+1)//2
    total += freq*arr[i]
print(total)
