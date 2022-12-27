# method one

sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
# maxwords = 0
# for i in sentences:
#     count = 0
#     x = i.split()
#     for j in x:
#         count = count+1
#     if count > maxwords:
#         maxwords = count
# print(maxwords)

# method two

# new_array=[]
# for sentence in sentences:
#     words_list=sentence.split()
#     length_of_elements=len(words_list)
#     new_array.append(length_of_elements)
# output=max(new_array)
# print(output)

# method three

lenght = max([len(i.split()) for i in sentences])
print(lenght)

