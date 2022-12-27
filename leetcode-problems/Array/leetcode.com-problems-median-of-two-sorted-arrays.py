nums1 = [1, 2]
nums2 = [3, 4]


list3 = nums1 + nums2
l = len(list3)
list3 = sorted(list3)

if l % 2 == 0:
    value = list3[int(l / 2)] + list3[int(l / 2) - 1]
    print(value / 2)
else:
    print(list3[int(l / 2)])
