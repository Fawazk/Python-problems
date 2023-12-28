def largestLocal(grid):
    n = len(grid)
    ans = [[0] * (n - 2) for _ in range(n - 2)]
    for i in range(n - 2):
        for j in range(n - 2):
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    ans[i][j] = max(ans[i][j], grid[x][y])
    return ans


print(
    largestLocal(
        [
            [20, 8, 20, 6, 16, 16, 7, 16, 8, 10],
            [12, 15, 13, 10, 20, 9, 6, 18, 17, 6],
            [12, 4, 10, 13, 20, 11, 15, 5, 17, 1],
            [7, 10, 14, 14, 16, 5, 1, 7, 3, 11],
            [16, 2, 9, 15, 9, 8, 6, 1, 7, 15],
            [18, 15, 18, 8, 12, 17, 19, 7, 7, 8],
            [19, 11, 15, 16, 1, 3, 7, 4, 7, 11],
            [11, 6, 5, 14, 12, 18, 3, 20, 14, 6],
            [4, 4, 19, 6, 17, 12, 8, 8, 18, 8],
            [19, 15, 14, 11, 11, 13, 12, 6, 16, 19],
        ]
    )
)
