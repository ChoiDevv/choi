# 2xn 타일링 2
# boj.kr/11727

import sys

n = int(sys.stdin.readline())
dp = [0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3, n + 1):
    dp[i] = 2 * (dp[i - 2]) + dp[i - 1]

print(dp[n])