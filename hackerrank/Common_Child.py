def commonChild(s1, s2):
    assert len(s1) == len(s2)
    n = len(s1) + 1
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, n):
            if s1[i-1] == s2[j-1]: dp[i][j] = dp[i-1][j-1]+1
            dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i-1][j])

    return dp[-1][-1]

print(commonChild(input(), input()))
