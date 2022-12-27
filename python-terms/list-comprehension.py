# Examples for list Comprehension

# same using normal for loop
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        if newlist == []:
            newlist.append(set())
        newlist[0].add(x)

print(newlist)

# using List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [{x: x for x in fruits if "a" in x}]

print(newlist)
