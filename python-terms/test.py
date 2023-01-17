# def prime(a):
#     count =0
#     for i in range(2,a):
#         if a%i != 0:
#             pass
#         else:
#             count = count+1
#     if count != 0:
#         return 0
#     else:
#         return 1
# for i in range(2,100):
#     test=prime(i)
#     if test == 1:
#         print(i)

# for num in range(2,10):
#     for i in range(2,num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)

for Number in range(1, 101):
    count = 0
    for i in range(2, Number):
        if Number % i == 0:
            count = count + 1
            break
    if count == 0 and Number != 1:
        print(Number, end="  ")


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

length = len(nums)
i = 0
while i < length:
    if nums[i] == val:
        nums.pop(i)
        length = length - 1
    else:
        i += 1
print(nums)
