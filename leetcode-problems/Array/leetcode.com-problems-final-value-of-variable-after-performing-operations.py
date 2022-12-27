#  def finalValueAfterOperations(self, operations: List[str]) -> int:
operation = ["--X", "X++", "X++"]
x = 0
for i in operation:
    if i == "--X" or i == "X--":
        x = x - 1
    else:
        x = x + 1
print(x)
