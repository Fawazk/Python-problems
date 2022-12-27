# The intersection() method returns a set that contains the similarity between two or more sets.

# Meaning: The returned set contains only items that exist in both sets, or in all sets if the comparison is done with more than two sets.

listone = []
listtwo = []
for j in range(4, 10):
    listone.append((j, j + 1))
for j in range(6, 12):
    listtwo.append((j, j + 1))
result = set(listone).intersection(listtwo)
print(result)


# function behind the function intersection
# 1
# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

# 2
# Python program to illustrate the intersection
# of two lists using set() method
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


# Driver Code
lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
print(intersection(lst1, lst2))
