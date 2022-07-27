accounts = [[1,2,3],[3,2,1]]
maxwealth = 0
for i in accounts:
    sum = 0
    for j in i:
        sum = sum + j
        if maxwealth <= sum:
            maxwealth = sum
print(maxwealth)


res = 0
temp = list(map(lambda x: sum(x), accounts))
print(max(temp))