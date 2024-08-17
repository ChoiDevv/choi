# 피보나치 수열
# f(n) = f(n-1) + f(n-2)

# 재귀
def fib(n):
    if (n <= 2): return 1
    return fib(n - 1) + fib(n - 2)

# DP
def dp(n):
    array = [0] * (n + 1)
    array[0] = 1
    array[1] = 1

    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    
    return array[n - 1]

print(dp(6))