def lisOtimised(s):
    # Stores at every i-th index, the
    # length of the longest increasing
    # subsequence ending with character i
    dp = [0] * 30

    # Size of string
    N = len(s)

    # Stores the length of LIS
    lis = -10 ** 9

    # Iterate over each
    # character of the string
    for i in range(N):

        # Store position of the
        # current character
        val = ord(s[i]) - ord('a')

        # Stores the length of LIS
        # ending with current character
        curr = 0

        # Check for all characters
        # less then current character
        for j in range(val):
            curr = max(curr, dp[j])

        # Include current character
        curr += 1

        # Update length of longest
        # increasing subsequence
        lis = max(lis, curr)

        # Updating LIS for current character
        dp[val] = max(dp[val], curr)

    # Return the length of LIS
    return lis


# Driver Code
if __name__ == '__main__':
    s = "abcfgffs"
    print(lisOtimised(s))