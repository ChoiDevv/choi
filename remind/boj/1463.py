# 1로 만들기 - 다시 풀어보기
# boj.kr/1463

import sys

n = int(sys.stdin.readline())
dp = [0] * 1000001 # 문제에서 10의 6제곱이 최댓값으로 지정되어 이에 대해 1을 더해줘 1에 해당하는 것이 1번째 인덱스라고 칭함.

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1 # 1을 뺀 최적의 해
    if i % 2 == 0: dp[i] = min(dp[i], dp[i // 2] + 1) # 1을 뺀 최적의 해와 인덱스가 2로 나누어지는 최적의 해를 비교해 가장 작은 값을 dp 테이블에 담음
    if i % 3 == 0: dp[i] = min(dp[i], dp[i // 3] + 1) # 위와 동일하나 나누어지는 값이 3

print(dp[i])