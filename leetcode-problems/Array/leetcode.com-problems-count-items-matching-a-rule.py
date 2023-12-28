items = [
    ["phone", "blue", "pixel"],
    ["computer", "silver", "phone"],
    ["phone", "gold", "iphone"],
]
ruleKey = "type"
ruleValue = "phone"
count = 0


rules = ["type", "color", "name"]
for i in items:
    items.insert(0, dict(zip(rules, i)))
    items.pop(1)
    if ruleKey in items[0]:
        if items[0][ruleKey] == ruleValue:
            count = count + 1
print(count)


# answer from leetcode

# dct = {"type": 0, "color": 1, "name": 2}
# key = dct[ruleKey]
# for item in items:
#     if item[key] == ruleValue:
#         count += 1
# print(count)
