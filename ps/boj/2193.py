# 이친수
# boj.kr/2193

import sys

n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[1] = 1

if (n > 1): dp[2] = 1

for i in range(3, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[n])

# 첫번째 풀이
def firstCode(n):
    dp = [[0] * 2 for _ in range(n + 1)]
    cnt = 0

    for i in range(1, 3):
        dp[i][0] = cnt
        cnt += 1

    cnt -= 1

    for i in range(1, 3):
        dp[i][1] = cnt
        cnt -= 1

    for i in range(3, n + 1):
        for j in range(2):
            dp[i][j] = dp[i - 2][j] + dp[i - 1][j]

    return sum(dp[n])