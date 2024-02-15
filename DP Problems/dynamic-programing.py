def minPathSum(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Initialize a 2D DP array to store the minimum cost at each position
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first row and column
    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the DP array by calculating the minimum cost at each position
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    # The bottom-right cell contains the minimum cost
    return dp[rows-1][cols-1]

# Example usage:
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

result = minPathSum(grid)
print("The minimum cost of the path is:", result)
