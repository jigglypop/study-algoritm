import sys
sys.stdin = open("11727.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [0] * 1001
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]
    dp[i] %= 10007
print(dp[N])
