# 1로 만들기
# @see https://www.acmicpc.net/problem/1463
# 1463

# dp[1] = 1
# dp[2] = 1
# dp[3] = 1
# dp[4] = dp[2] + 1
# dp[10] = dp[5] + 1 ? dp[9] + 1 > 가장 작은 값을 dp[10]에 저장

# 즉, dp[n]에 dp[n // 2] 또는 dp[n // 3] + 1과 dp[n - 1] + 1을 비교해서 가장 작은 값을 먼저 저장하고 꺼내서 사용

"""
import sys

n = int(sys.stdin.readline())
dp = [0] * 1000001 # [0] * (n + 1)을 하면 index error 발생함. 나는 dp[1], dp[2], dp[3]에 대한 값을 미리 설정.
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0: dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0: dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[n])
"""

import sys


n = int(sys.stdin.readline())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0: dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0: dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[n])

# 위의 방식과 차이는 값을 미리 설정하지 않고 어차피 dp[1] = 0이고 dp[2]부터 값을 설정하면 되기에 선언의 형태를 다르게 함.
# -> 문제에서는 10의 6제곱까지라고 나와있어 상관없으나 메모리 관련해서는 틀릴 수도 있다 생각.