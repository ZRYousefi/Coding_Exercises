
# Recursive:

def lcs(pattern_1, pattern_2, len_1, len_2):
    if len_1 == 0 or len_2 == 0:
        return 0
    if pattern_1[len_1 - 1] == pattern_2[len_2 - 1]:
        return 1 + lcs(pattern_1, pattern_2, len_1 - 1, len_2 - 1)
    else :
        return max(lcs(pattern_1, pattern_2, len_1 - 1, len_2), lcs(pattern_1, pattern_2, len_1, len_2 - 1))
pattern_1 = "RGBGARGA"
pattern_2 = "BGRARG"
print("Lenght of LCS is: ", lcs(pattern_1, pattern_2, len(pattern_1), len(pattern_2)))

# Dynamic programming :

def lcs(pattern_1, pattern_2):
    m = len(pattern_1)
    n = len(pattern_2)
    # dp will store solutions as the iteration goes on
    dp = [
        [None] * (n + 1) for item in range(m + 1)
    ]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif pattern_1[i - 1] == pattern_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else :
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
pattern_1 = "RGBGARGA"
pattern_2 = "BGRARG"
print("Length of LCS: ", lcs(pattern_1, pattern_2))


'''The DP method has lower time complexity; it is O(mn), where m and n are the length of the input string or array.
DP is a faster approach than the recursive one, with the time complexity of O(n*2m).
Dynamic programming (DP) is not memory optimized. We used a 2D array that has the length of m*n. So, the space complexity is (m*n).
Recursive method, in a worst-case scenario, the highest memory it will occupy will be m+n, basically the total length of the inputted string.
Today’s modern computer is sufficient to handle this amount of memory.'''