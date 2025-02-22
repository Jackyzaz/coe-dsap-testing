def gridChallenge(grid):
    for i in range(len(grid)):
        grid[i] = "".join(sorted(grid[i]))

    for i in range(len(grid[0])):
        for j in range(len(grid) - 1):
            if grid[j][i] <= grid[j + 1][i]:
                continue
            else:
                return "NO"
    return "YES"
