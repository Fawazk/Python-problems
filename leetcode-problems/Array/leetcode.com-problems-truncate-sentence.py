class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        return " ".join(s[0:k])


s = Solution()
string = "Hello how are you Contestant"
k = 4
print(s.truncateSentence(string, k))
