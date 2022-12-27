# import string
# from typing import List

# class Solution:
#     def uniqueMorseRepresentations(self, words: List[str]) -> int:


#         morse = [".-","-...","-.-.","-..",".","..-.","--.","....",
#                     "..",".---","-.-",".-..","--","-.","---",".--.",
#                     "--.-",".-.","...","-","..-","...-",".--","-..-",
#                     "-.--","--.."]

#         dic = {}
#         code = ""
#         array = []
#         count = 0
#         alphabet = string.ascii_lowercase
#         for i in range(len(alphabet)):
#             dic[alphabet[i]] = morse[i]
#         for i in words:
#             for j in i:
#                 if j in dic:
#                     code = code + ''.join(dic[j])
#             if code in array:
#                 count = count
#             else:
#                 count = count+1
#             array.append(code)
#             code = ''

#         return count


# Leetcode solution


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        MORSE = [
            ".-",
            "-...",
            "-.-.",
            "-..",
            ".",
            "..-.",
            "--.",
            "....",
            "..",
            ".---",
            "-.-",
            ".-..",
            "--",
            "-.",
            "---",
            ".--.",
            "--.-",
            ".-.",
            "...",
            "-",
            "..-",
            "...-",
            ".--",
            "-..-",
            "-.--",
            "--..",
        ]

        seen = {"".join(MORSE[ord(c) - ord("a")] for c in word) for word in words}
        print(seen)
        return len(seen)


s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
